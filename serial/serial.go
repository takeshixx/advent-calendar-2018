package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"math/rand"
	"net"
	"reflect"
	"strconv"
	"strings"
	"time"
)

func writeConnection(conn net.Conn, challs []chalStruct, messages chan string) {
	for len(messages) > 0 {
		<-messages
	}
	var correct int
	if len(challs) == 0 {
		conn.Write([]byte("Something went wrong on our side :( connect again"))
		conn.Close()
		return
	}
	for {
		for _, chal := range challs {
			messages <- string(chal.challenge + "\n")
			buffer := make([]byte, 1400)
			dataSize, err := conn.Read(buffer)
			if err != nil {
				log.Println("Connection has closed")
				return
			}

			//This is the message you received
			data := buffer[:dataSize-1]
			int_input, _ := strconv.Atoi(string(data))
			log.Printf("Client Answered: %d", int_input)
			if int_input == chal.result {
				correct++
				if correct >= len(challs) {
					messages <- "SOLVED\n"
					conn.Close()
				}
				messages <- "Congratulations... This was correct \n"
			} else {
				messages <- "Wrong\n"
				log.Printf("Client got challenge wrong.. Lets kick him")
				conn.Close()
				return
			}
		}
	}
}

func readConnection(conn net.Conn, messages chan string) {
	afterCh := time.After(10 * time.Second)
	for {
		select {
		case d := <-messages:
			if strings.Contains(d, "Wrong") {
				conn.Write([]byte(d))
				conn.Close()
			}
			if strings.Contains(d, "SOLVED") {
				success, err := ioutil.ReadFile("./success")
				if err != nil {
					log.Fatal("Success File not there ?")
				}
				conn.Write(success)
				conn.Close()
			}
			conn.Write([]byte(d))
			log.Println("Channel Sending:", d)
			break
		case <-afterCh:
			log.Printf("Time's up for %s", conn.RemoteAddr())
			conn.Write([]byte("Your Time is up. Tschingle Fail\n"))
			conn.Close()
			break
		}
	}
}

func main() {
	var challs map[string][]chalStruct
	challs = make(map[string][]chalStruct)

	messages := make(map[string](chan string))
	fmt.Println("The server is listening on Port 6")
	listener, err := net.Listen("tcp", "localhost:6")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("The server2 is listening on Port 66")
	listener2, err := net.Listen("tcp", "localhost:66")
	if err != nil {
		log.Fatal(err)
	}
	go acceptLoop(listener, challs, messages)
	acceptLoop(listener2, challs, messages) // run in the main goroutine
}

func RandomInt(min int, max int) int {
	r := rand.New(rand.NewSource(time.Now().UnixNano()))
	p := r.Perm(max - min + 1)
	return p[min]
}

func create_challenge() (string, int) {
	var function_operators = map[string]interface{}{
		"+": func(x int, y int) int { return x + y },
		"-": func(x int, y int) int { return x - y },
		"*": func(x int, y int) int { return x * y },
		"/": func(x int, y int) int { return x / y },
	}

	keys := reflect.ValueOf(function_operators).MapKeys()
	rand_operator := keys[rand.Intn(len(keys))].Interface().(string)
	n1 := RandomInt(0, 100000)
	// Avoiding Division by Zero
	var n2 int
	if rand_operator == "/" {
		n2 = RandomInt(1, 100000)
	} else {
		n2 = RandomInt(0, 100000)
	}
	res := function_operators[rand_operator].(func(int, int) int)(n1, n2)
	return strconv.Itoa(n1) + rand_operator + strconv.Itoa(n2), res
}

type chalStruct struct {
	challenge string
	result    int
}

func acceptLoop(l net.Listener, challs map[string][]chalStruct, m map[string](chan string)) {
	defer l.Close()
	for {
		c, err := l.Accept()
		if err != nil {
			log.Fatal(err)
		}
		defer l.Close()
		var ipChallenges []chalStruct
		local_port := strings.Split(c.LocalAddr().String(), ":")
		ip := strings.Split(c.RemoteAddr().String(), ":")
		log.Printf("New connection found -> %s\n", ip[0])
		if local_port[1] == "6" {
			amount := RandomInt(2, 10)
			for i := 0; i <= amount; i++ {
				chal, result := create_challenge()
				test := chalStruct{challenge: chal, result: result}
				ipChallenges = append(ipChallenges, test)
			}
			log.Printf("Created new Challenges for IP: %s", ip[0])
			m[ip[0]] = make(chan string)
			challs[ip[0]] = ipChallenges
			go readConnection(c, m[ip[0]])
		} else {
			if val, ok := challs[ip[0]]; ok {
				go writeConnection(c, val, m[ip[0]])
			} else {
				c.Write([]byte("It is SERIAL important that you do other Stuff first\n"))
				log.Printf("Sending Go Away Message to %s\n", ip[0])
				c.Close()
			}
		}
	}
}
