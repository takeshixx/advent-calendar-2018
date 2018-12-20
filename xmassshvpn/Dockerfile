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
RUN mkdir /run/sshd || true
RUN useradd -m santa
RUN usermod --password "\$6\$xmas\$xYqOoLcl9Ew0acHPI69OhpPuLfpCiEzEzpSKrR0f1.09oKP94kVB43M93P2hCmmi49q99a6izW6HevK9YZjM91" santa
RUN mkdir /home/santa/.ssh/
COPY ssh_host* /etc/ssh/
RUN chmod 600 /etc/ssh/ssh_host*
COPY sshd_config /etc/ssh/sshd_config
COPY dhcpd.conf /etc/dhcpd.conf
RUN touch /usr/src/app/leases
COPY run.sh .
CMD ["/usr/src/app/run.sh"]
