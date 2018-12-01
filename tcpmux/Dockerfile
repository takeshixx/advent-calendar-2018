FROM ubuntu:18.04
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y xinetd python3
WORKDIR /usr/src/app
COPY wishlist.py .
RUN chmod +x wishlist.py
COPY wishlist.xinetd /etc/xinet.d/wishlist
COPY echo.xinetd /etc/xinet.d/echo
COPY time.xinetd /etc/xinet.d/time
CMD ["/usr/sbin/xinetd", "-dontfork"]