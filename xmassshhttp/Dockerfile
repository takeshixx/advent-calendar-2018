FROM ubuntu:18.04
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y nginx openssh-server git python3 python3-pip
WORKDIR /usr/src/app
RUN git clone https://github.com/draplater/tcpmux.git
RUN chmod +x /usr/src/app/tcpmux/tcpmux.py
RUN pip3 install uvloop
COPY nginx.conf /etc/nginx/nginx.conf
#RUN echo "sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin" >> /etc/passwd
#RUN echo "sshd:x:74:" >> /etc/group
RUN mkdir /run/sshd || true
RUN useradd -m santa
RUN usermod --password "\$6\$xmas\$xYqOoLcl9Ew0acHPI69OhpPuLfpCiEzEzpSKrR0f1.09oKP94kVB43M93P2hCmmi49q99a6izW6HevK9YZjM91" santa
COPY ssh_host* /etc/ssh/
RUN chmod 600 /etc/ssh/ssh_host*
COPY sshd_config /etc/ssh/sshd_config
COPY ascii /home/santa/ascii
COPY wrapper.sh /home/santa/wrapper.sh
COPY run.sh .
CMD ["/usr/src/app/run.sh"]
