func minAddToMakeValid(S string) int {
	re, _ := regexp.Compile("\\(\\)")

	S = re.ReplaceAllString(S, "")
	sum := len(S)

	for {
		S = re.ReplaceAllString(S, "")

		if sum > len(S) {
			sum = len(S)
		} else if sum == len(S) {
			return len(S)
		}
	}
}
