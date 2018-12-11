FROM ubuntu:18.04
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential git autoconf libssl-dev zlib1g-dev libpam0g-dev openssh-server
WORKDIR /usr/src/app
RUN git clone https://github.com/openssl/openssl.git && \
        cd openssl && \
        git checkout OpenSSL_1_0_2-stable && \
        ./config && \
        make -j2 && \
        make install || true
COPY openssh_v6.8_none_cipher.patch .
RUN git clone https://github.com/openssh/openssh-portable.git && \
        cd openssh-portable && \
        git checkout V_6_8 && \
        git apply ../openssh_v6.8_none_cipher.patch && \
        autoreconf -i && \
        ./configure \
            --with-pam \
            --with-ssl-engine \
            --with-ssl-dir=../openssl && \
        make -j2 || true
RUN echo "sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin" >> /etc/passwd
RUN echo "sshd:x:74:" >> /etc/group
RUN mkdir /var/empty || true
RUN useradd -m santa
RUN usermod --password "\$6\$xmas\$xYqOoLcl9Ew0acHPI69OhpPuLfpCiEzEzpSKrR0f1.09oKP94kVB43M93P2hCmmi49q99a6izW6HevK9YZjM91" santa
COPY ssh_host* /usr/local/etc/
RUN chmod 600 /usr/local/etc/ssh_host*
COPY sshd_config /usr/local/etc/sshd_config
COPY ascii /home/santa/ascii
COPY wrapper.sh /home/santa/wrapper.sh
CMD ["/usr/src/app/openssh-portable/sshd", "-D", "-p", "2222", "-o", "Ciphers=none"]