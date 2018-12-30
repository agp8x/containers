FROM alpine:3.7
RUN apk add --update --no-cache py3-flask py3-cryptography && adduser -D flask
USER flask
EXPOSE 5000
ADD cbcmustdie.py cbcmustdie.key flag.txt /
ENV FLASK_APP=cbcmustdie.py
CMD ["flask", "run", "-h", "0.0.0.0"]
