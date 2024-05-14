"""
Find all possible shortest paths
"""

import math


class Solution:
    def findSequences(self, startWord, targetWord, wordList):
        sequences = []
        new_seq = []
        words_to_be_removed = []
        s = set(wordList)
        length = len(startWord)
        min_len_seq = math.inf
        q = []
        q.append(([startWord], 1))
        if startWord in s:
            s.remove(startWord)
        while q:
            size = len(q)
            while size != 0:
                words, level = q.pop(0)
                size -= 1
                sw = words[-1]
                for i in range(length):
                    for alpha in range(97, 123):
                        if i == 0:
                            new_word = chr(alpha) + sw[1:]
                        elif i == length - 1:
                            new_word = sw[0 : length - 1] + chr(alpha)
                        else:
                            new_word = sw[0:i] + chr(alpha) + sw[i + 1 :]

                        if new_word in s:
                            words_to_be_removed.append(new_word)
                            word2 = words.copy()
                            word2.append(new_word)
                            q.append((word2, level + 1))
                            if new_word == targetWord:
                                min_len_seq = min(len(word2), min_len_seq)
                                sequences.append((word2, level + 1))

            for word in words_to_be_removed:
                if word in s:
                    s.remove(word)

            words_to_be_removed = []

        for seq, level in sequences:
            if level == min_len_seq:
                new_seq.append(seq)
        return new_seq


soln = Solution()
print(soln.findSequences("der", "dfs", ["des", "der", "dfr", "dgt", "dfs"]))
print(soln.findSequences("gedk", "geek", ["geek", "gefk"]))
print(
    soln.findSequences(
        "toon", "plea", ["poon", "plee", "same", "poie", "plea", "plie", "poin"]
    )
)
