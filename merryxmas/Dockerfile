FROM ubuntu:18.04
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y nginx
WORKDIR /usr/src/app
RUN mkdir www
COPY index.html www/index.html
COPY music.m4a www/music.m4a
COPY patrick.gif www/patrick.gif
COPY snowstorm.js www/snowstorm.js
COPY nginx.conf /etc/nginx/nginx.conf
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]

