FROM ubuntu:18.04

RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y gnupg gnupg2 ca-certificates 

RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y python2.7-dev python-pip libssl-dev cmake git

WORKDIR /usr/src/app
RUN \
	git clone https://github.com/keystone-engine/keystone.git && \
	cd keystone/bindings/python && \
	make install && \
	cd ../.. && \
	mkdir build && \
	cd build && \
	../make-share.sh && \
	make install && \
	ldconfig

RUN \
	pip install unicorn
	
	

COPY server.py .
RUN chmod +x server.py
COPY success .

EXPOSE 16
CMD ["python", "/usr/src/app/server.py"]
