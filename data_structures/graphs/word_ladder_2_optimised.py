"""
Find all possible shortest paths
"""


class Solution:
    def findSequences(self, startWord, targetWord, wordList):
        seq = []
        ans = []
        word_level_hash = dict()
        s = set(wordList)
        length = len(startWord)
        q = []
        q.append((startWord, 1))
        word_level_hash[startWord] = 1
        if startWord in s:
            s.remove(startWord)
        while q:
            size = len(q)
            while size != 0:
                word, level = q.pop(0)
                size -= 1
                sw = word
                for i in range(length):
                    for alpha in range(97, 123):
                        if i == 0:
                            new_word = chr(alpha) + sw[1:]
                        elif i == length - 1:
                            new_word = sw[0 : length - 1] + chr(alpha)
                        else:
                            new_word = sw[0:i] + chr(alpha) + sw[i + 1 :]

                        if new_word in s:
                            word_level_hash[new_word] = level + 1
                            s.remove(new_word)
                            q.append((new_word, level + 1))

        seq.append(targetWord)
        self.generate_all_sequences(startWord, targetWord, word_level_hash, seq, ans)
        return ans

    def generate_all_sequences(self, start, end, word_dict, seq, ans):
        if end == start:
            s = seq.copy()
            s.reverse()
            ans.append(s)
            return
        level = word_dict[end]
        length = len(end)
        for i in range(length):
            for alpha in range(97, 123):
                if i == 0:
                    new_word = chr(alpha) + end[1:]
                elif i == length - 1:
                    new_word = end[0 : length - 1] + chr(alpha)
                else:
                    new_word = end[0:i] + chr(alpha) + end[i + 1 :]

                if new_word in word_dict and word_dict[new_word] == level - 1:
                    seq.append(new_word)
                    self.generate_all_sequences(start, new_word, word_dict, seq, ans)
                    seq.pop()


soln = Solution()
print(soln.findSequences("der", "dfs", ["des", "der", "dfr", "dgt", "dfs"]))
print(soln.findSequences("gedk", "geek", ["geek", "gefk"]))
# print(
# soln.findSequences(
# "toon", "plea", ["poon", "plee", "same", "poie", "plea", "plie", "poin"]
# )
# )
