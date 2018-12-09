FROM ubuntu:18.04
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential git autoconf libssl-dev zlib1g-dev
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
            --with-ssl-engine \
            --with-ssl-dir=/usr/src/app/openssl && \
        make -j2 || true
CMD ["/usr/src/app/openssh-portable/sshd", "-o", "-o Ciphers=none"]