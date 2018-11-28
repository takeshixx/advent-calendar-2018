# Advent Calendar of Advanced Cyber Fun 2018
Gimme m0ar cyber funZ!1

# Agenda

| Port | Challenge | Path |
| ---- | --------- | ---- |
| 1    | TCPMUX ([RFC1078](https://tools.ietf.org/html/rfc1078)) service: Assigned TCP port 1 by IANA ([RFC1700](https://tools.ietf.org/html/rfc1700)). | [tcpmux](tcpmux) 

# Potential Challenges

* Websocket server mit ner Rechnung zum proggn für Lösung
* SCTP Port
* .net RPC interface
* Shellcode generator mit Antwort einer billigen rechnung mov eax,1; add eax,2
* X-JFAG
  * Serial interface. 2 Ports.. one reading the other writing
* BPF port. Mit source code rausgeben wo ein spezielles Packet mit Scapy gesendet werden muss.
* https://ma.ttias.be/googles-quic-protocol-moving-web-tcp-udp/
* Port 0 Just for fun 
* TLS-SRP
* TLSv1.3
* TLS with client cert
* IPv6 (only?), is there anything special with IPv6 that we could do?
* HTTP server with **XMAS** method
* JAVA RMI?
* HTTP over UDP
* Port knocking sequenece - send TCP packet to 2018 first in order to make port accessible.
* HTTP server that requires special user-agent and referrer header.
* UDP port with DTLS?
* iptable/BPF rules with a pattern where useless/reserved/unnecessary bits have to be set or else the packets will be dropped.
* SSH server on TCP 22
    * Probably recompile sshd with [none cipher](https://serverfault.com/questions/116875/how-can-i-disable-encryption-on-openssh/606367#606367)
    * Restrict commands via authorized_keys file
* Message Send Procotol 2 on TCP 18 ([RFC1312](https://tools.ietf.org/html/rfc1312))
    * Message Send Protocol ([RFC1159](https://tools.ietf.org/html/rfc1159))
    * On [Wikipedia](https://en.wikipedia.org/wiki/Message_Send_Protocol)
    * Supports COOKIE (UDP) and SIGNATURE