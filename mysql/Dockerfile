FROM mysql:latest

EXPOSE 3306
ENV MYSQL_DATABASE=db
ENV MYSQL_ROOT_PASSWORD=root
COPY ./students_database.sql /docker-entrypoint-initdb.d/
