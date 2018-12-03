FROM ubuntu:18.04
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y apache2
WORKDIR /usr/src/app
COPY passwd.xmas .
COPY passwd.xmas.attr .
COPY passwd.xmas.old .
ADD www /var/www/site
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ADD apache2-vhost.conf /etc/apache2/sites-enabled/000-default.conf
CMD /usr/sbin/apache2ctl -D FOREGROUND
