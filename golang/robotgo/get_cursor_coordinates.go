package main

import (
	"fmt"
	"time"
	"github.com/go-vgo/robotgo"
)

func get() {
	time.Sleep(2 * time.Second)
  x, y := robotgo.GetMousePos()
	fmt.Println("pos:", x, y)
}

func main() {
	mouse()
}
