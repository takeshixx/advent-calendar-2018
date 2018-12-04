FROM ubuntu:18.04
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y nginx
WORKDIR /usr/src/app
COPY nginx.conf /etc/nginx/nginx.conf
CMD ["/usr/bin/nginx", "-g", "daemon off;"]

