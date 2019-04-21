package main

import "fmt"
import "time"
import "strconv"

func main(){
  time.Sleep(2 * time.Second)
  unixtime := strconv.FormatInt(time.Now().UTC().Unix(), 10)
  
  fmt.Println("Unix Time is:", time.Now().Unix())
  fmt.Println("Unix Time using string conversion:", unixtime)
}
