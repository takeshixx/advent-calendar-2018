FROM ubuntu:18.04
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y dnsmasq dnsutils socat
WORKDIR /usr/src/app
COPY hosts /etc/hosts
COPY run.sh .
CMD ["./run.sh"]
