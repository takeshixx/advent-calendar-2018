FROM ubuntu:18.04

RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y gnupg gnupg2 ca-certificates 

RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y python python-pip && \
  pip install unicorn keystone


WORKDIR /usr/src/app
COPY server.py .
RUN chmod +x server.py
COPY success .

EXPOSE 16
CMD ["python", "/usr/src/app/server.py"]
