FROM alpine:3.7
EXPOSE 80
VOLUME ["/etc/icinga2", "/etc/icingaweb2"]
RUN apk add --update apache2 php7-apache2 icingaweb2-module-director && sed -i -e "s/^#LoadModule rewrite_module/LoadModule rewrite_module/" /etc/apache2/httpd.conf
ADD ["start.sh", "/"]
CMD ["sh", "/start.sh"]