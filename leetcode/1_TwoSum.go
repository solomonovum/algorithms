package main

import "fmt"

func twoSum(nums []int, target int) []int {
	complementMap := make(map[int]int)

	for i, value := range nums {
		// 현재 값을 기준으로 target에 대한 보수가 hash에 있는지 확인
		_, keyCheck := complementMap[value]

		if keyCheck {
			// index만 return
			return []int{complementMap[value], i}

		} else {
			// 합해서 target이 되는 수로 hash의 key값을 설정
			complementMap[target-value] = i
		}
	}
	return nil
}

func main() {
	nums := []int{2, 7, 11, 15}
	target := 18

	ans := twoSum(nums, target)

	fmt.Println(ans)
}
