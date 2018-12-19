package main

import (
	"crypto/rand"
	"crypto/rsa"
	"crypto/tls"
	"crypto/x509"
	"encoding/pem"
	"math/big"
	"fmt"
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

NW2ODB0laI0syozU6Xr5gJxkFKenZ+fXiLq/ggACLW8qZISFhu9C30F+HKL6X6Y4`

func main() {
	if len(os.Args) < 3 {
		fmt.Printf("Usage: %s host port [cert] [key]\n", os.Args[0])
		os.Exit(1)
	}
	host := os.Args[1]
	port := os.Args[2]
	var config *tls.Config
	if len(os.Args) > 3 {
		cert := os.Args[3]
		key := os.Args[4]
		pem, err := tls.LoadX509KeyPair(cert, key)
		if err != nil {
			panic(err)
		}
		config = &tls.Config{Certificates: []tls.Certificate{pem}}
	} else {
		config = generateTLSConfig()
	}
	addr := fmt.Sprintf("%s:%s", host, port)
	err := echoServer(addr, config)
	if err != nil {
		panic(err)
	}
}

func echoServer(addr string, config *tls.Config) error {
	fmt.Printf("Starting listener on %s\n", addr)
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

func generateTLSConfig() *tls.Config {
	key, err := rsa.GenerateKey(rand.Reader, 1024)
	if err != nil {
		panic(err)
	}
	template := x509.Certificate{SerialNumber: big.NewInt(1)}
	certDER, err := x509.CreateCertificate(rand.Reader, &template, &template, &key.PublicKey, key)
	if err != nil {
		panic(err)
	}
	keyPEM := pem.EncodeToMemory(&pem.Block{Type: "RSA PRIVATE KEY", Bytes: x509.MarshalPKCS1PrivateKey(key)})
	certPEM := pem.EncodeToMemory(&pem.Block{Type: "CERTIFICATE", Bytes: certDER})

	tlsCert, err := tls.X509KeyPair(certPEM, keyPEM)
	if err != nil {
		panic(err)
	}
	return &tls.Config{Certificates: []tls.Certificate{tlsCert}}
}
