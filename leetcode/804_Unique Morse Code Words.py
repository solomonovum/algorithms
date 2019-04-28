class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
                # mapping Morse with str
        concat_str = []
        full_str = []
        
        for index, word in enumerate(words):
            concat_str.clear()
            for element in word:
                concat_str.append(Morse[ord(element) - ord('a')])
            full_str.append(''.join(concat_str))

        # insert to map
        return len(set(full_str))


Morse = [".-",
 "-...",
 "-.-.",
 "-..",
 ".",
 "..-.",
 "--.",
 "....",
 "..",
 ".---",
 "-.-",
 ".-..",
 "--",
 "-.",
 "---",
 ".--.",
 "--.-",
 ".-.",
 "...",
 "-",
 "..-",
 "...-",
 ".--",
 "-..-",
 "-.--",
 "--.."]

f = Solution()

input = ["gin", "zen", "gig", "msg"]

print(f.uniqueMorseRepresentations(input))
