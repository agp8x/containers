FROM alpine:3.7
RUN apk add --update icinga2 postgresql-client
ADD ["start.sh", "init.sh", "/"]
VOLUME ["/etc/icinga2"]
VOLUME ["/var/lib/icinga2"]

CMD ["sh", "/start.sh"]