#!/bin/sh
if [ ! -f /etc/icinga2/.docker_initialized ]; then
	echo "[ICINGA] initialize...."
	sh /init.sh
fi
echo "[ICINGA] start daemon..."
mkdir -p /run/icinga2/cmd
chown -R icinga:icingacmd /run/icinga2
/usr/sbin/icinga2 daemon -c /etc/icinga2/icinga2.conf
