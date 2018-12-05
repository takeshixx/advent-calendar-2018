# Advent Calendar of Advanced Cyber Fun 2018
Gimme m0ar cyber funZ!1

# Agenda

| Port | Challenge | Path |
| ---- | --------- | ---- |
| 1    | TCPMUX ([RFC1078](https://tools.ietf.org/html/rfc1078)) service: Assigned TCP port 1 by IANA ([RFC1700](https://tools.ietf.org/html/rfc1700)). | [tcpmux](tcpmux) 
| 2    | XMASbleed (CVE-2014-0160): Heartbleed with christmas fun! | [xmasbleed](xmasbleed)
| 3    | HTTPoSCTP: HTTP over SCTP, a poor man's implementation of [draft-natarajan-http-over-sctp-00.txt](https://tools.ietf.org/html/draft-natarajan-http-over-sctp-00). | [sctphttp](sctphttp)
| 4    | KnockKnock: A webserver that is only accessible after knocking on TCP port sequence `42 23 16 15 8`. | [knockknock](knockknock)
| 5    | HTTPS with Client Certificate: Accessing the webserver requires a client certificate that includes `christmas` in the Common Name field. | [tlsclientcert](tlsclientcert)
| 6    | SERIAL Challenge. It is required to talk to two sockets. One read only and one write only. | [serial](serial)
| 9    | BPF filter with magic keyword. C code will be provided. | [bpf](bpf)

# Potential Challenges

* Websocket server mit ner Rechnung zum proggn für Lösung
* .net RPC interface
* Shellcode generator mit Antwort einer billigen rechnung mov eax,1; add eax,2
* X-JFAG
  * Serial interface. 2 Ports.. one reading the other writing
* [QUIC](https://ma.ttias.be/googles-quic-protocol-moving-web-tcp-udp/)
    * Some implementations are available
        * [Playing with QUIC](https://www.chromium.org/quic/playing-with-quic)
        * [quic-py](https://github.com/ZhukovAlexander/quic-py)
        * [quic-go](https://github.com/lucas-clemente/quic-go)
    * [HTTP over QUIC](https://tools.ietf.org/html/draft-ietf-quic-http-03)
        * it's a current draft, could be interesting to implement a poor man's version.
* Port 0 Just for fun
* TLS
    * with funny cipher suites
    * algorithms that are not widely supported
* TLS-SRP
* TLSv1.3
    * any special cipher suites?
    * which clients are supported?
* TLS with client cert
    * requires to be signed by Christmas Inc. CA
    * required different types of certs
* IPv6
    * IPv6 only service
    * TLS port with client cert, requires IPv6 address in CN
* HTTP server with **XMAS** method
* JAVA RMI?
* HTTP over UDP
    * Nginx/Apache with socat
    * probably implement UDP handler for aiohttp?
        * should work by implementing a [low-level server](https://docs.aiohttp.org/en/stable/web_lowlevel.html#run-a-basic-low-level-server) with [loop.create_unix_server](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server) and socat.
        * maybe implement a loop.create_udp_server?
* HTTP server that requires special user-agent and referrer header.
* UDP port with DTLS
* iptable/BPF rules with a pattern where useless/reserved/unnecessary bits have to be set or else the packets will be dropped.
* SSH server on TCP 22
    * Probably recompile sshd with [none cipher](https://serverfault.com/questions/116875/how-can-i-disable-encryption-on-openssh/606367#606367)
    * Restrict commands via authorized_keys file
* Message Send Procotol 2 on TCP 18 ([RFC1312](https://tools.ietf.org/html/rfc1312))
    * Message Send Protocol ([RFC1159](https://tools.ietf.org/html/rfc1159))
    * On [Wikipedia](https://en.wikipedia.org/wiki/Message_Send_Protocol)
    * Supports COOKIE (UDP) and SIGNATURE
* TCP multiplexer
    * run HTTP/HTTPS and SSH on the same port
        * probably just fork [this](https://github.com/draplater/tcpmux)
    * run HTTP/HTTPS and any other protocol on the same port?
* HTTP Proxy that injects JavaScript snow into pages
* SSH with layer 3 VPN routing
    * HTTP server running on local IP address accessible via SSH layer 3 VPN
