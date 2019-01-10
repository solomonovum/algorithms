func topKFrequent(words []string, k int) []string {
    wordcounting := make(map[string]int)

	// word counting
	for _, word := range words {
		if value, ok := wordcounting[word]; ok {
			wordcounting[word] = value + 1
		} else {
			wordcounting[word] = 1
		}
	}

	// make heap
	data := new(maxheap)
	heap.Init(data)

	for word, count := range wordcounting {
		heap.Push(data, Words{word, count})
	}

	// get return string by maxheap
	ret := make([]string, 0)

	for i := 0; i < k; i++ {
		maxstring := heap.Pop(data).(Words)
		ret = append(ret, maxstring.word)
	}

	return ret 
}

type Words struct {
	word  string
	count int
}

type maxheap []Words

func (h maxheap) Len() int {
	return len(h)
}

func (h maxheap) Less(i, j int) bool {
	if h[i].count == h[j].count {
		return h[i].word < h[j].word
	} else {
		return h[i].count > h[j].count
	}
}

func (h maxheap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *maxheap) Push(x interface{}) {
	*h = append(*h, x.(Words))
}

func (h *maxheap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}
