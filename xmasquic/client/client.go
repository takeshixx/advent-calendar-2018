package main

import (
	"crypto/tls"
	"fmt"
	"io"
	"os"
	quic "github.com/lucas-clemente/quic-go"
)

func main() {
	if len(os.Args) < 3 {
		fmt.Printf("Usage: %s host port\n", os.Args[0])
		os.Exit(1)
	}
	host := os.Args[1]
	port := os.Args[2]
	addr := fmt.Sprintf("%s:%s", host, port)
	err := clientMain(addr)
	if err != nil {
		panic(err)
	}
}

func clientMain(addr string) error {
	session, err := quic.DialAddr(addr, &tls.Config{InsecureSkipVerify: true}, nil)
	if err != nil {
		return err
	}

	stream, err := session.OpenStreamSync()
	if err != nil {
		return err
	}
	_, err = stream.Write([]byte("Hello?"))
	if err != nil {
		return err
	}

	buf := make([]byte, 4096)
	_, err = io.ReadAtLeast(stream, buf, 10)
	if err != nil {
		return err
	}
	fmt.Printf("Client: Got '%s'\n", buf)

	return nil
}
