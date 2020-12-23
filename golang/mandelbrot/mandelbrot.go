package main

import (
	"fmt"
	"math/cmplx"
)

type Point struct {
	x, y float64
}

func main() {
	p := Point{0.3, 0}
	fmt.Println(converging(p, 50))
}

func converging(p Point, maxIterations int) (bool, int) {
	c1 := complex(p.x, p.y)
	z := complex(0, 0)
	for i := 1; i < maxIterations; i++ {
		z = z*z + c1
		if cmplx.Abs(z) > 2 {
			return false, i
		}
	}
	return true, 0
}
