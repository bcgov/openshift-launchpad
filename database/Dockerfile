# Base image
FROM postgres:10-alpine

# Copy any custom SQL files to run during init
ADD *.sql /docker-entrypoint-initdb.d/

# Set the working directory to container entrypoint
WORKDIR /docker-entrypoint-initdb.d