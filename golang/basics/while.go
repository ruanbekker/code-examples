package main

import "fmt"
import "time"

func main() {
	count := 0
	for count <= 10 {
		fmt.Println("Count is:", count)
		time.Sleep(1 * time.Second)
		count++
	}
}
