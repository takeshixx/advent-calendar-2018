# TCPMUX Service

A simple service that implements TCPMUX ([RFC1078](https://tools.ietf.org/html/rfc1078)). The following description from RFC sums up more or less the complete protocol definition:

```
The Protocol

   A TCP client connects to a foreign host on TCP port 1.  It sends the
   service name followed by a carriage-return line-feed <CRLF>.  The
   service name is never case sensitive.  The server replies with a
   single character indicating positive ("+") or negative ("-")
   acknowledgment, immediately followed by an optional message of
   explanation, terminated with a <CRLF>.  If the reply was positive,
   the selected protocol begins; otherwise the connection is closed.

Service Names

   The name "HELP" is reserved.  If received, the server will output a
   multi-line message and then close the connection.  The reply to the
   name "HELP" must be a list of the service names of the supported
   services, one name per line.
```

The service provides echo, time and wishlist. The wishlist service is Santa's custom service for creating wishlists!

## Building & Running

```bash
docker build -t day01_tcpmux .
docker run -d --restart=always -p 1:1 --name=day01 day01_tcpmux
```