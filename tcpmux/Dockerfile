FROM ubuntu:18.04
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y xinetd 
WORKDIR /usr/src/app
COPY wishlist.py .
COPY wishlist.xinetd /etc/xinet.d/wishlist
COPY echo.xinetd /etc/xinet.d/echo
COPY time.xinetd /etc/xinet.d/time
RUN systemctl enable xinetd
RUN service xinetd restart