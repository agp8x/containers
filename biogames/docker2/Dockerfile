FROM alpine:edge

RUN set -ex &&\
	echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories && \
	apk upgrade --update &&\
	apk add --update nodejs proj4-dev \
		geos-dev \
		py-geos \
		gdal \
		gdal-dev \
		py-gdal \
		py-psycopg2 \
		jpeg-dev \
		postgresql-dev \
		bash \
		py-virtualenv \
		gcc \
		zlib-dev \
		python2-dev \
		libc-dev \
		sqlite-dev \
		postgresql-client

ADD ["start.sh", "/"]

VOLUME ["/biogames", "/venv"]
EXPOSE 8000

ENTRYPOINT ["/start.sh"]
CMD ["runserver", "0.0.0.0:8000"]
