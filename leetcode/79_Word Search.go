var dx = [4]int{1, -1, 0, 0}
var dy = [4]int{0, 0, 1, -1}

func exist(board [][]byte, word string) bool {
	if len(board) <= 0 {
		return false
	}

	// run
	for x := 0; x < len(board); x++ {
		for y := 0; y < len(board[0]); y++ {
			if dfs(x, y, 0, board, word) {
				return true
			}
		}
	}
	return false
}

func dfs(x, y, count int, board [][]byte, word string) bool {
	// exit confition
	if board[x][y] == word[count] && board[x][y] != 0 {
		if count == len(word)-1 {
			return true
		}

		// go EWSN
		count++
		temp := board[x][y]
		board[x][y] = 0

		var ret bool
		for index := 0; index < 4; index++ {
			nx := x + dx[index]
			ny := y + dy[index]

			// boundary check
			if nx >= 0 && nx < len(board) && ny >= 0 && ny < len(board[0]) {
				ret = dfs(nx, ny, count, board, word)
				if ret {
					board[x][y] = temp
					return true
				}
			}
		}
		// restore
		board[x][y] = temp
		return ret
	} else {
		return false
	}
}
