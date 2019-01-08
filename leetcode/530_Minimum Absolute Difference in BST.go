/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func getMinimumDifference(root *TreeNode) int {
    v := make([]int, 0)
    
    dfs(root, &v)
    
    min := math.MaxInt32

    for index := 0; index < len(v) - 1; index++ {
        min = int(math.Min(float64(min), (float64(v[index+1]) - float64(v[index]))))
    }
    
    return min
}

func dfs(root *TreeNode, v *[]int) {
    if root == nil {
        return
    }
        
    if root.Left != nil {
        dfs(root.Left, v)
    }
    
    *v = append(*v, root.Val)
    
    if root.Right != nil {
        dfs(root.Right, v)
    }
 }
