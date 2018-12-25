package mom

// MedianOfMedians is used as a pivot selection in the quickselect algorithm
func MedianOfMedians(data []int, left, right, nTh, groupSize int) int {
	for {
		// get median pivot
		pivoIndex := getMedianPivot(data, left, right, groupSize)

		// do partitioning
		pivoIndex = partition(data, left, right-1, pivoIndex)

		if nTh == pivoIndex {
			return nTh // find the position of nTh element
		} else if nTh < pivoIndex {
			right = pivoIndex // now, find left side
		} else {
			left = pivoIndex + 1 // now, find right side
		}
	}
}

// get median of medians pivot by iteration
func getMedianPivot(data []int, left, right, groupSize int) int {
	for {
		size := right - left

		if size < groupSize {
			return partitionN(data, left, right, groupSize)
		}

		// index is increased by a group size
		for index := left; index < right; index += groupSize {
			subRight := index + groupSize

			// check boundary
			if subRight > right {
				subRight = right
			}

			// get median
			median := partitionN(data, index, subRight, groupSize)

			// move each median to the front of container
			data[median], data[left+(index-left)/groupSize] =
				data[left+(index-left)/groupSize], data[median]
		}

		// update the end of medians
		right = left + (right-left)/groupSize
	}
}

// partiton data into two parts (left, right), those less than a certain element
func partition(data []int, left, right, pivotIndex int) int {
	pivotValue := data[pivotIndex]

	// move pivot to end
	data[pivotIndex], data[right] = data[right], data[pivotIndex]

	// partition
	lowindex := left
	for highIndex := left; highIndex < right; highIndex++ {
		if data[highIndex] < pivotValue {
			data[highIndex], data[lowindex] = data[lowindex], data[highIndex]
			lowindex++
		}
	}

	// move pivot to its final place
	data[lowindex], data[right] = data[right], data[lowindex]

	return lowindex
}

// sort if data is lower than group size (generally 5)
func partitionN(data []int, left, right, groupSize int) int {
	// insertion sort
	for standardIndex := left + 1; standardIndex < right; standardIndex++ {
		for comparedIndex := standardIndex - 1; comparedIndex >= left; comparedIndex-- {
			if data[comparedIndex+1] < data[comparedIndex] {
				data[comparedIndex+1], data[comparedIndex] = data[comparedIndex], data[comparedIndex+1]
			}
		}
	}

	// get median index
	medianindex := left + groupSize/2

	// check rightside boundary
	if medianindex >= right {
		medianindex = right - 1
	}

	return medianindex
}
