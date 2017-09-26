#!/bin/sh

if [ ! -d /mnt/proc_doc ]; then
	if [ -d /mnt/proc ]; then
		umount /proc
		mount -o bind /mnt/proc /proc
		mkdir /mnt/proc_doc
		mount -t proc none /mnt/proc_doc
	fi
fi

collectd -f