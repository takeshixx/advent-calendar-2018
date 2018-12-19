FROM ubuntu:18.04
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y wget git
RUN wget https://dl.google.com/go/go1.11.2.linux-amd64.tar.gz && \ 
	    tar -C /usr/local -xzf go1.11.2.linux-amd64.tar.gz
ENV PATH $PATH:/usr/local/go/bin
ENV GOPATH /root/go
ENV PATH $PATH:/usr/local/go/bin
RUN go get github.com/lucas-clemente/quic-go
WORKDIR /usr/src/app
COPY server.go .
CMD ["go", "run", "server.go", "0.0.0.0", "21", "/certs/fullchain1.pem", "/certs/privkey1.pem"]

