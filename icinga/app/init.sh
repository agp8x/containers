#!/bin/sh

apk del icinga2 && apk add icinga2

echo "[INIT] load DB scheme"
PGPASSWORD=$POSTGRES_PASSWORD psql -h $POSTGRES_HOST -U $POSTGRES_USER -d $POSTGRES_USER < /usr/share/icinga2-ido-pgsql/schema/pgsql.sql

echo "[INIT] setup DB credentials"
cat > /etc/icinga2/features-available/ido-pgsql.conf <<EOF
/**
 * The db_ido_pgsql library implements IDO functionality
 * for PostgreSQL.
 */

library "db_ido_pgsql"

object IdoPgsqlConnection "ido-pgsql" {
  user = "$POSTGRES_USER"
  password = "$POSTGRES_PASSWORD"
  host = "$POSTGRES_HOST"
  database = "$POSTGRES_USER"
}
EOF

echo "[INIT] prepare-dirs"
/usr/lib/icinga2/prepare-dirs /etc/init.d/icinga2
echo "[INIT] enable ido-pgsql"
icinga2 feature enable ido-pgsql checker command
echo "[INIT] setup api"
icinga2 api setup

echo "[INIT] done."
echo $(date) > /etc/icinga2/.docker_initialized