# Advent Calendar of Advanced Cyber Fun 2018
Gimme m0ar cyber funZ!1

## Agenda

| Port | Challenge | Path |
| ---- | --------- | ---- |
| 1    | TCPMUX ([RFC1078](https://tools.ietf.org/html/rfc1078)) service: Assigned TCP port 1 by IANA ([RFC1700](https://tools.ietf.org/html/rfc1700)). | [tcpmux](tcpmux) 
| **2**    | XMASbleed (CVE-2014-0160): Heartbleed with christmas fun! | [xmasbleed](xmasbleed)
| 3    | HTTPoSCTP: HTTP over SCTP, a poor man's implementation of [draft-natarajan-http-over-sctp-00.txt](https://tools.ietf.org/html/draft-natarajan-http-over-sctp-00). | [sctphttp](sctphttp)
| 4    | KnockKnock: A webserver that is only accessible after knocking on TCP port sequence `42 23 16 15 8`. | [knockknock](knockknock)
| 5    | HTTPS with Client Certificate: Accessing the webserver requires a client certificate that includes `christmas` in the Common Name field. | [tlsclientcert](tlsclientcert)
| 6    | SERIAL Challenge. It is required to talk to two sockets. One read only and one write only. | [serial](serial)
| 7    | XMASHTTP: A webserver that implements a special **XMAS** HTTP method | [xmashttp](xmashttp)
| 8    | TLS ChaCha: A HTTPS server that is only accessible with ChaCha20 based ciper suites. | [tlschacha](tlschacha)
| **9**    | eBPF filter with magic keyword. C code will be provided. | [ebpf](ebpf)
| 10   | .NET Remoting Server. pcap will be provided. | [remoting](remoting)
| 11   | PlainSSH: A patched OpenSSH server that only allows connections with "none" ciphers. Requires a patched OpenSSH client, maybe provide patch for OpenSSH v6.8. | [plainssh](plainssh)
| 12   | TLS13: A HTTPS server that only supports TLSv1.3. | [tls13](tls13)
| 13   | TCPReserved: A service that is only accessible when the reserved bits in the TCP header are set. Similar to [evil bit](https://blog.benjojo.co.uk/post/evil-bit-RFC3514-real-world-usage) but on layer 4. | [reservedbits](reservedbits)
| 14   | XMASSSHHTTP: A TCP multiplexer port that runs HTTPS and SSH. | [xmassshhttp](xmassshhttp)
| 15   | A websocket Server which needs a specific input to print the success message | [websocket](websocket)
| **16**   | ASMoverTCP: A service that prints byte code with arithmetic operations. | [assembly](assembly)
| 17   | TLS-SRP: A Nginx HTTPS server that only supports TLS-SRP with a weak password. | [tlssrp](tlssrp)
| 18   | Message Send Procotol 2: Python implementation of [RFC1312](https://tools.ietf.org/html/rfc1312). Users need to send a message to a specific user with a signature. Code for signature creation/checking will be provided. | [msp2](msp2)
| 19   | TCPImages: A challenge-response authentication that sends images with random codes. Clients have to send random code back in the same TCP session. | [tcpimages](tcpimages)
| 20   | XMASDoH: A DNS Queries over HTTPS (DoH) ([RFC8484](https://tools.ietf.org/html/rfc8484)) server with a special **xmas** TXT record. | [xmasdoh](xmasdoh)
| 21   | XMASQUIC: A simple QUIC server. | [xmasquic](xmasquic)
| 22   | TBD | TBD
| **23**   | SSH Layer 3 VPN: A internal host that is only accessible from local IP address via layer 3 VPN. | TBD
| 24   | TBD | TBD

## Potential Challenges

* TLS with client cert
    * requires to be signed by an official CA and do other checks. only publish the code.
* Special HTTP server
    * HTTP server that requires special user-agent and referrer header.
* JAVA RMI
    * A simple remote interface where users have to implement a simple client that calls a function.
    * Just slightly change the [Hello World](https://docs.oracle.com/javase/8/docs/technotes/guides/rmi/hello/hello-world.html) example.
* HTTP Proxy that injects JavaScript snow into pages
* Port Hunter
    * A service that just prints a port number which will be opened temporarily.
    * Port wil change every several seconds.
    * Users will have to automate it: connect to main port, fetch the port number, connect to the second port.
    * Could include multiple protocols like TCP/UDP/SCTP.

## Development Setup

Create a development VM with pre-installed Docker:

```bash
vagrant up
vagrant ssh
```

Within the VM, you can build the Docker containers:

```bash
cd /vagrant/tcpmux
sudo docker build -t day01_tcpmux .
sudp docker run -d --restart=always -p 1:1 --name=day01 day01_tcpmux
```

The VM creates a second host-only interface by default, which should expose the services.
