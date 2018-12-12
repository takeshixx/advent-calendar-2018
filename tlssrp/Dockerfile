FROM ubuntu:18.04
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y nginx openssl
WORKDIR /usr/src/app
COPY passwd.xmas .
COPY nginx /etc/nginx/nginx.conf

