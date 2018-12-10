FROM ubuntu:18.04
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential git wget
WORKDIR /usr/src/app
RUN git clone https://github.com/openssl/openssl.git && \
        cd openssl && \
        git checkout OpenSSL_1_1_1-stable && \
        ./config && \
        make -j2 && \
        make install || true
RUN wget https://ftp.pcre.org/pub/pcre/pcre-8.42.tar.gz && tar xzvf pcre-8.42.tar.gz
RUN git clone https://github.com/nginx/nginx.git && \
        cd nginx && \
        git checkout release-1.14.1 && \
        auto/configure \
            --with-http_stub_status_module \
            --without-http_charset_module \
            --without-http_gzip_module \
            --without-http_ssi_module \
            --without-http_userid_module \
            --without-http_access_module \
            --without-http_auth_basic_module \
            --without-http_autoindex_module \
            --without-http_geo_module \
            --without-http_map_module \
            --without-http_split_clients_module \
            --without-http_referer_module \
            --without-http_proxy_module \
            --without-http_fastcgi_module \
            --without-http_uwsgi_module \
            --without-http_scgi_module \
            --without-http_memcached_module \
            --without-http_limit_conn_module \
            --without-http_limit_req_module \
            --without-http_empty_gif_module \
            --without-http_browser_module \
            --without-http_upstream_ip_hash_module \
            --without-http_upstream_least_conn_module \
            --without-http_upstream_keepalive_module \
            --with-pcre=../pcre-8.42 \
            --with-pcre-jit \
            --with-http_ssl_module \
            --with-openssl=/usr/src/app/openssl \
            --with-ld-opt="-L/usr/src/app/openssl" \
            --with-openssl-opt=enable-tls1_3 && \
        make -j2 && \
        make install
COPY nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /var/log/nginx
RUN touch /var/log/nginx/access.log
RUN touch /var/log/nginx/error.log
CMD ["/usr/src/app/nginx/objs/nginx", "-c", "/etc/nginx/nginx.conf", "-g", "daemon off;"]