FROM ubuntu:18.04
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y xinetd python3
WORKDIR /usr/src/app
COPY wishlist.py .
RUN chmod +x wishlist.py
COPY wishlist.xinetd /etc/xinetd.d/wishlist
COPY echo.xinetd /etc/xinetd.d/echo
COPY time.xinetd /etc/xinetd.d/time
COPY tcpmux.xinetd /etc/xinetd.d/tcpmux
EXPOSE 1
CMD ["/usr/sbin/xinetd", "-dontfork"]
