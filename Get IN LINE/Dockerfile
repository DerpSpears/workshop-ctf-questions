FROM php:8.0-apache


WORKDIR /var/www/html


COPY src/index.php index.php
COPY src/flag.txt flag.txt





RUN chown -R root:root /var/www/html



RUN chmod -R 555 /var/www/html && \
    chmod 444 /var/www/html/index.php && \
    chmod 444 /var/www/html/flag.txt


RUN apt-get clean && rm -rf /var/lib/apt/lists/*


EXPOSE 8001
