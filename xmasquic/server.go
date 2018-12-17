package main

import (
	"crypto/rand"
	"crypto/rsa"
	"crypto/tls"
	"crypto/x509"
	"encoding/pem"
	"fmt"
	"math/big"
	"os"
	quic "github.com/lucas-clemente/quic-go"
)

const xmas = `Wow, that was QUIC!

                          |
                        \ ' /
                      -- (*) --
                         >*<
                        >0<@<
                       >>>@<<*
                      >@>*<0<<<
                     >*>>@<<<@<<
                    >@>>0<<<*<<@<
                   >*>>0<<@<<<@<<<
                  >@>>*<<@<>*<<0<*<
    \*/          >0>>*<<@<>0><<*<@<<
___\\U//___     >*>>@><0<<*>>@><*<0<<
|\\ | | \\|    >@>>0<*<0>>@<<0<<<*<@<<  
| \\| | _(UU)_ >((*))_>0><*<0><@<<<0<*<
|\ \| || / //||.*.*.*.|>>@<<*<<@>><0<<<
|\\_|_|&&_// ||*.*.*.*|_\\db//_               
""""|'.'.'.|~~|.*.*.*|     ____|_
    |'.'.'.|   ^^^^^^|____|>>>>>>|
    ~~~~~~~~         '""""|------'

gS3sgimI95DYGorXd/hj9tJlPBucjPJHUOe8coxqOVPbFcGLtpt5tdoGu2SVnO2w`

func main() {
	if len(os.Args) < 5 {
		fmt.Printf("Usage: %s host port cert key\n", os.Args[0])
		os.Exit(1)
	}
	host := os.Args[1]
	port := os.Args[2]
	cert := os.Args[3]
	key := os.Args[4]
	addr := fmt.Sprintf("%s:%s", host, port)
	err := echoServer(addr, cert, key)
	if err != nil {
		panic(err)
	}
}

func echoServer(addr string, cert string, key string) error {
	pem, err := tls.LoadX509KeyPair(cert, key)
	if err != nil {
		panic(err)
	}
	config := &tls.Config{Certificates: []tls.Certificate{pem}}
	listener, err := quic.ListenAddr(addr, config, nil)
	if err != nil {
		return err
	}
	for {
		sess, err := listener.Accept()
		if err != nil {
			return err
		}
		go handleConnection(sess)
	}
}

func handleConnection(sess quic.Session) error {
	fmt.Printf("Got a new connection from: %s\n", sess.RemoteAddr().String())
	stream, err := sess.AcceptStream()
	if err != nil {
		panic(err)
	}
	_, err = stream.Write([]byte(xmas))
	return err
}
