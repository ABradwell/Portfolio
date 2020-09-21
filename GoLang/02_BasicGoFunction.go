package main

import (
	"fmt"
)

func statusPrint(state int8) {
	var m = map[int8]string{
		0 : "Idle",
		1 : "Start",
		2 :  "Forward",
		3 :  "Fast",
		-1 :  "Reverse",
	}
	if state > 3 || state < -1 {
		fmt.Println("Invalid State")
	}else{
		fmt.Println("State is " + m[state])
	}
	

	return
}

func main() {
	var i int8
	for i = -1; i < 5; i++ {
		statusPrint(i)
	}
}