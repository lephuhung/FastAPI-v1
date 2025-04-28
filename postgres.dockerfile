FROM postgres:15

COPY ./populate.sql /docker-entrypoint-initdb.d/

RUN chmod a+r /docker-entrypoint-initdb.d/populate.sql