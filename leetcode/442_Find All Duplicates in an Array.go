func findDuplicates(nums []int) []int {
    var res []int
    for i:=0; i<len(nums); i++ {
        index := int(math.Abs(float64(nums[i]))) - 1
        if nums[index] < 0 {
            res = append(res, index+1)
        }
        nums[index] *= -1
    }
    return res
}
