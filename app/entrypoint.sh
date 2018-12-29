!/bin/sh
psql -U ${PGUSER} -c "SELECT 1 FROM pg_database WHERE datname = '${Database_db_name}'" | grep -q 1 || psql -U ${PGUSER} -c "CREATE DATABASE ${Database_db_name}"
# psql -U ${PGUSER} -c "CREATE USER ${Database_db_user} WITH PASSWORD '${Database_db_pass}'"
# psql -U ${PGUSER} -c "ALTER DATABASE ${Database_db_name} OWNER TO ${Database_db_user}"
psql -U ${PGUSER} -d ${Database_db_name} -c "CREATE EXTENSION IF NOT EXISTS HSTORE"
pushkin --configuration /app/pushkinconfig.ini --upgrade-db
exec "$@"