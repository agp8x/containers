Usage
=====

1. create a *postgres.env* file:

		POSTGRES_USER=<user>
		POSTGRES_PASSWORD=<secret>
		POSTGRES_DB=<dbname>

	* user and db are optional
		* user defaults to postgres
		* db defaults to <user>

#. `docker-compose up -d`
#. launch a browser and finish installation on localhost:10080/
	* use PostgreSQL as database
	* use credentials from postgres.env file

Requirements

* docker (1.13.0+)
* docker-compose (1.10.0+)
