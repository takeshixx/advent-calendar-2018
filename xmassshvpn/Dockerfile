FROM ubuntu:18.04
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y \
    openssh-server \
    isc-dhcp-server \
    iproute2 \
    libirs-export160
WORKDIR /usr/src/app
#RUN echo "sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin" >> /etc/passwd
#RUN echo "sshd:x:74:" >> /etc/group
RUN mkdir /run/sshd || true
RUN useradd -m santa
RUN usermod --password "\$6\$xmas\$xYqOoLcl9Ew0acHPI69OhpPuLfpCiEzEzpSKrR0f1.09oKP94kVB43M93P2hCmmi49q99a6izW6HevK9YZjM91" santa
RUN mkdir /home/santa/.ssh/
COPY santa_authorized_keys /home/santa/.ssh/authorized_keys
RUN chown -R santa:santa /home/santa/.ssh/
RUN chmod -R 700 /home/santa/.ssh/
COPY ssh_host* /etc/ssh/
RUN chmod 600 /etc/ssh/ssh_host*
COPY sshd_config /etc/ssh/sshd_config
COPY dhcpd.conf /etc/dhcpd.conf
COPY run.sh .
CMD ["/usr/src/app/run.sh"]
