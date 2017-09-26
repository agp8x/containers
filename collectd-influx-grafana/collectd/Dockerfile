FROM alpine:3.6

RUN apk --update search -qe 'collectd-*' | xargs apk add

ADD ["run.sh", "/"]
CMD ["/run.sh"]