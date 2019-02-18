func permute(nums []int) [][]int {
   	var result [][]int

	perm(nums, 0, len(nums), len(nums), &result)

	return result 
}

func perm(arr []int, depth int, n int, k int, result *[][]int) {
	if depth == k {
		elementsize := len(arr)
		copyone := make([]int, elementsize)
		copy(copyone, arr)
		*result = append(*result, copyone)
		return
	}

	for i := depth; i < n; i++ {
		arr[i], arr[depth] = arr[depth], arr[i]
		perm(arr, depth+1, n, k, result)
		arr[i], arr[depth] = arr[depth], arr[i]
	}
}
