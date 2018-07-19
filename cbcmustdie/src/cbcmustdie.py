import os
import json
import base64

from flask import Flask, request, render_template_string, make_response
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

app = Flask('cbcmustdie')

@app.route('/')
def index():
    template = """
    {% if username %}
    <p>Hello {{ username }}.</p>
    <p><a href="/logout">Logout.</a></p>
    {% else %}
    <p><a href="/login">Please login first.</a></p>
    {% endif %}

    {% if is_admin %}
    <p>Here is your flag: {{ flag }}</p>
    {% else %}
    <p>Only admins can see the flag.</p>
    {% endif %}
    """

    session = read_session_cookie()
    if session is None:
        username = None
        is_admin = False
    else:
        username = session['username']
        is_admin = session['is_admin']

    with open('flag.txt') as f:
        flag = f.read()

    return render_template_string(template,
            username=username, is_admin=is_admin, flag=flag)


@app.route('/login', methods=['GET', 'POST'])
def login():
    template = """
    <form method="post" action="/login">
    <p><label>Username: <input type="text" name="username"></label></p>
    <p><button>Login</button></p>
    </form>
    """

    if request.method == 'POST':
        response = make_response()
        set_session_cookie(response,
                username=request.form.get('username'), is_admin=False)
        response.status_code = 303
        response.headers['Location'] = '/'
        return response
    else:
        return render_template_string(template)


@app.route('/logout')
def logout():
    response = make_response()
    response.status_code = 303
    response.headers['Location'] = '/'
    response.set_cookie('session', '', expires=0)
    return response


def read_session_cookie():
    """Read the CBC encrypted and base64 encoded session cookie."""
    try:
        session_cookie = request.cookies['session']
    except KeyError:
        return None
    try:
        session = json.loads(decrypt_cbc(base64.b64decode(session_cookie)).decode())
    except Exception:
        raise
        return None
    return session


def set_session_cookie(response, username, is_admin):
    """Write a CBC encrypted and base64 encoded session cookie.

    The decoded and decrypted cookie is a JSON blob:
    {"is_admin":false,"username":"john"}
    """
    session = {"is_admin": is_admin, "username": username}
    json_value = json.dumps(session, separators=(',',':'), sort_keys=True)
    # The json_value will look like this (because of separators and sort_keys):
    # {"is_admin":false,"username":"john"}
    ciphertext = encrypt_cbc(json_value.encode())
    response.set_cookie('session', base64.b64encode(ciphertext))


def get_aes_key():
    """Read a randomly generated AES key from a file."""
    with open('cbcmustdie.key', 'rb') as f:
        key = f.read()
        assert len(key) == 32
        return key


def encrypt_cbc(plaintext):
    """AES encryption in CBC mode with PKCS7 padding.
    
    IV (16 bytes) is prepended to the actual ciphertext.
    """
    backend = default_backend()
    padder = padding.PKCS7(128).padder()
    plaintext = padder.update(plaintext) + padder.finalize()
    key = get_aes_key()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    return iv + encryptor.update(plaintext) + encryptor.finalize()


def decrypt_cbc(ciphertext):
    """AES decryption in CBC mode with PKCS7 padding.
    
    IV is taken from the first 16 bytes.
    """
    backend = default_backend()
    key = get_aes_key()
    # First 16 bytes contain the IV, everything after is ciphertext
    iv, real_ciphertext = ciphertext[:16], ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(real_ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext

