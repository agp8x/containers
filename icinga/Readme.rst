* `docker-compose exec db sh`
	* `psql -U postgres`
		* `CREATE DATABASE icingaweb2 WITH OWNER icinga ENCODING utf8;`
		* `CREATE DATABASE icingadirector WITH OWNER icinga ENCODING utf8;`
* `docker-compose exec icinga icinga2 node wizard`
	* `docker-compose icinga restart`
* setup token: Logs from web (or data/web/etc/setup.token)
* icinga container restart for changes from director