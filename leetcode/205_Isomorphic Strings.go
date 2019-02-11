func isIsomorphic(s string, t string) bool {
	m := make([]int, 256)
	n := make([]int, 256)

	for i := 0; i < len(s); i++ {
		if m[int(s[i])] != n[int(t[i])] {
			return false
		}
		m[int(s[i])] = i + 1
		n[int(t[i])] = i + 1
	}
	return true
}
