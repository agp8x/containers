FROM alpine:3.6

EXPOSE 80
ADD ["sass.sh", "settings_local.build.py", "/"]
RUN apk add --update python3 python3-dev git g++ nodejs-npm mariadb-dev mariadb-client-libs \
 && ln -s /sass.sh /usr/bin/sass \
 && git clone https://github.com/fsinfuhh/Bitpoll \
 && rm -r /Bitpoll/.git \
 && pip3 install -r /Bitpoll/requirements.txt \
 && pip3 install pyscss mysqlclient \
 && npm install --global coffeescript \
 && cd /Bitpoll \
 && mv /settings_local.build.py /Bitpoll/bitpoll/settings_local.py \
 && python3 manage.py migrate \
 && python3 manage.py compilestatic \
 && apk del nodejs-npm mariadb-dev git g++ python3-dev
WORKDIR /Bitpoll
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:80"]
