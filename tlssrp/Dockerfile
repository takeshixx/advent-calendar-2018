FROM ubuntu:18.04
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y apache2
WORKDIR /usr/src/app
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
COPY apache2-vhost.conf /etc/apache2/sites-enabled/
COPY passwd.xmas .
RUN mkdir www
COPY success www/
RUN chown -R www-data:www-data www
RUN a2enmod ssl
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
