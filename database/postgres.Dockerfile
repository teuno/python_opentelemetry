FROM postgres:13-alpine
COPY init.sql /docker-entrypoint-initdb.d/