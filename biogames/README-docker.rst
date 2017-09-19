Biogames-docker
===============

Run biogames server with docker compose

Requirements
============

* docker engine
* docker-compose >= 1.10.0

Usage
=====

Configuration
-------------

Put any configuration files in *biogames/biogames/settings.d/*

*006_docker_db.py* is prepared for a connection to the postgres-database configured with docker-compose



First Startup
-------------

1. Start DB: `docker-compose up -d db`
2. Apply schema: `docker-compose run web migrate` (Initializes virtualenv, too)
3. Start web + celery `docker-compose up -d`

Alternative to #2: Use Admin-access (see below) to import db-dump

Preparation for production:

* See *biogames/INSTALL.txt*
* Especially collectstatic and compilemessages
* Environment, dependencies and service management is maintained by docker-compose


Operational Handling
--------------------


* Start: `docker-compose up -d`
* Shutdown: `docker-compose down`
* Maintenance (Django)
	* Start django shell: `docker-compose run web shell`
	* Obtain system shell:
		1. `docker-compose run web shell`
		2. `import os`
		3. `os.system("bash")`

* Admin: `docker-compose -f docker-compose.yml -f docker-compose.admin.yml run {web,celery,db}`
	* maps */mnt* to *admin/{web,celery,db}*