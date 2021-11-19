/*
Basic Method calling in golang
Author: Aiden Stevenson Bradwell  ||  abrad060@uottawa.ca  ||  300064655
Janurary 30th, 2020
Created for: CSI2120 (Programming Paradigms)
*/

package main

import (
	"fmt"
	"math"
	"errors"
)

type NegError struct {
	num float64 // negative number
}

func rootDivN(num float64, n int) (res float64, err error) {
	if num < 0.0 {
		str := fmt.Sprint("Main NegError: Negative number ", num)
		return 0, errors.New(str)
	}
	if n == 0 {
		return 0, errors.New("Main Div0: Division by 0")
	}
	res = math.Sqrt(num) / float64(n)
	return res, nil
}

func main() {
	divs := []int{2, 10, 3, 0}
	nums := []float64{511.8, 0.65, -3.0, 2.123}

	for i, num := range nums {
		fmt.Printf("%d) sqrt(%f)/%d = ", i, num, divs[i])
		res, err := rootDivN(num, divs[i])
		if err == nil {
			fmt.Printf("%f\n", res)
		}else{
			fmt.Printf("%s\n", err)
		}
	}
}