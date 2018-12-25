package mom

import (
	"fmt"
	"math"
	"math/rand"
	"reflect"
	"sort"
	"testing"
	"time"
)

var maximum int = math.MaxUint16 * 10

type TestData struct {
	argument int
}

var testdata = []TestData{
	{0},
	{maximum - 1},
	{maximum / 3},
	{maximum / 7},
}

func TestMom(t *testing.T) {
	for _, data := range testdata {
		groupSize := 5

		numberRange := maximum
		input := generateRandomSlice(maximum, numberRange)

		inputForSort := make([]int, maximum)
		copy(inputForSort, input)

		// median of medians
		startTime := time.Now()
		result := MedianOfMedians(input, 0, maximum, data.argument, groupSize)
		fmt.Println("Median Of Medians")
		fmt.Println("nTh index :", result, "/", "result :", input[result])
		elapsedTime := time.Since(startTime)
		fmt.Printf("elapsed time: %s\n", elapsedTime)

		// sort
		startTime = time.Now()
		sort.Ints(inputForSort)
		fmt.Println("general sort")
		fmt.Println("nTh index :", data.argument, "/", "result :", inputForSort[data.argument])
		elapsedTime = time.Since(startTime)
		fmt.Printf("elapsed time: %s\n", elapsedTime)

		// are they the same?
		if !reflect.DeepEqual(input[data.argument], inputForSort[data.argument]) {
			t.Error("not the same")
		}

		fmt.Printf("\n")
	}
}

// this generates a slice of random number
func generateRandomSlice(size, numberRange int) []int {
	// check size
	if size < 0 {
		return nil
	}

	slice := make([]int, size, size)
	rand.Seed(time.Now().UnixNano())
	for i := 0; i < size; i++ {
		slice[i] = rand.Intn(numberRange) - rand.Intn(numberRange)
	}
	return slice
}
