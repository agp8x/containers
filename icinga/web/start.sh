#!/bin/sh
if [ ! -f /etc/icingaweb2/.docker_initialized ]; then
	/usr/share/webapps/icingaweb2/bin/icingacli setup config directory --group www-data;
	echo "Please take note of this setup token. This should be pasted into icingaweb2 setup web page: "
	/usr/share/webapps/icingaweb2/bin/icingacli setup token create;
	
	echo "<VirtualHost *:80>" > /etc/apache2/conf.d/icingaweb2.conf
	echo "" >> /etc/apache2/conf.d/icingaweb2.conf
	icingacli setup config webserver apache >> /etc/apache2/conf.d/icingaweb2.conf
	echo "" >> /etc/apache2/conf.d/icingaweb2.conf
	echo "</VirtualHost>" >> /etc/apache2/conf.d/icingaweb2.conf
	
	echo $(date) > /etc/icingaweb2/.docker_initialized
fi	
mkdir -p /run/apache2
httpd -DFOREGROUND
