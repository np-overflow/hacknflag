#!/bin/sh

PORT=${PORT:-"8080"}
docker rm -f kevin-php-1-running
docker run -d -p ${PORT}:${PORT} -e PORT=${PORT} --name kevin-php-1-running kevin-php-1
