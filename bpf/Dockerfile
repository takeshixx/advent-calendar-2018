FROM ubuntu:18.04

RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y gnupg gnupg2 lsb-release ca-certificates linux-headers-$(uname -r)

RUN \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4052245BD4284CDD && \
  echo "deb https://repo.iovisor.org/apt/$(lsb_release -cs) $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/iovisor.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y python3 bcc-tools libbcc-examples python3-bcc python3-pip && \
  pip3 install scapy


WORKDIR /usr/src/app
COPY run.py .
RUN chmod +x run.py
COPY parse.c .
COPY success .

EXPOSE 9
CMD ["python3", "/usr/src/app/run.py"]
