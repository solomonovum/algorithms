func numJewelsInStones(J string, S string) int {
	// make table
	alphabetSize := 'z' - 'A' + 1

	alphabetTable := make([]int, alphabetSize)

	// fiil table value
	for _, value := range J {
		alphabetTable[value-'A']++
	}

	// get count
	count := 0

	for _, value := range S {
		if 1 == alphabetTable[value-'A'] {
			count++
		}
	}
	return count
}
