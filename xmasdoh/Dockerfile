FROM ubuntu:18.04
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y dnsmasq dnsutils python3 python3-pip
RUN pip3 install doh-proxy
WORKDIR /usr/src/app
COPY dnsmasq.conf .
COPY run.sh .
CMD ["./run.sh"]
