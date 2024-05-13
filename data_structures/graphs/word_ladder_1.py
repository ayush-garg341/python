"""
Find the shortest sequence from start word to target word.
- Changing one letter at a time.
"""


class Solution:
    def wordLadderLength(self, startWord, targetWord, wordList):
        s = set(wordList)
        length = len(startWord)
        q = []
        q.append((startWord, 1))
        if startWord in s:
            s.remove(startWord)
        while q:
            sw, level = q.pop(0)
            for i in range(length):
                for alpha in range(97, 123):
                    if i == 0:
                        new_word = chr(alpha) + sw[1:]
                    elif i == length - 1:
                        new_word = sw[0 : length - 1] + chr(alpha)
                    else:
                        new_word = sw[0:i] + chr(alpha) + sw[i + 1 :]

                    if new_word in s:
                        s.remove(new_word)
                        q.append((new_word, level + 1))
                        if new_word == targetWord:
                            return level + 1

        return 0


soln = Solution()
print(soln.wordLadderLength("der", "dfs", ["des", "der", "dfr", "dgt", "dfs"]))
print(soln.wordLadderLength("gedk", "geek", ["geek", "gefk"]))
print(
    soln.wordLadderLength(
        "toon", "plea", ["poon", "plee", "same", "poie", "plea", "plie", "poin"]
    )
)
