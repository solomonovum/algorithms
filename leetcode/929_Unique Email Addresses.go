func numUniqueEmails(emails []string) int {
	validstring := make(map[string]bool)

	for _, email := range emails {
		// depart from @
		s1 := strings.Split(email, "@")

		// remove .
		s2 := strings.Replace(s1[0], ".", "", -1)

		// remove after +
		s3 := strings.Split(s2, "+")

		// insert unordered_set
		validstring[s3[0]+s1[1]] = true
	}

	return len(validstring)
}
