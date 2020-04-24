/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func bfs(node *TreeNode, value int) (int, int) {
	runQueue := []*TreeNode{}
	runQueue = append(runQueue, node)

	replaceQueue := []*TreeNode{}

	parentMap := make(map[int]int)
	Depth := 0

	// find integer value
	for nil != runQueue[0] {
		if value == runQueue[0].Val {
			break
		}

		if runQueue[0].Left != nil {
			replaceQueue = append(replaceQueue, runQueue[0].Left)
			parentMap[runQueue[0].Left.Val] = runQueue[0].Val
		}

		if runQueue[0].Right != nil {
			replaceQueue = append(replaceQueue, runQueue[0].Right)
			parentMap[runQueue[0].Right.Val] = runQueue[0].Val
		}

		runQueue = runQueue[1:]

		if 0 == len(runQueue) {
			for 0 != len(replaceQueue) {
				runQueue = append(runQueue, replaceQueue[0])
				replaceQueue = replaceQueue[1:]
			}
			Depth++
		}
	}
	return parentMap[value], Depth
}

func isCousins(root *TreeNode, x int, y int) bool {
    // integer value exception handling
	if (x < 1 || x > 100) || (y < 1 || y > 100) {
		return false
	}

	parentX, depthX := bfs(root, x)
	parentY, depthY := bfs(root, y)

	if parentX != parentY {
		if depthX == depthY {
			return true
		}
	}

	return false
}
