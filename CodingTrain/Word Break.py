#lru_cache
class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:

		@lru_cache

		def travel(index):
			result = False
			if index >= len(s):
				return True

			for word in wordDict:
				if s[index: index + len(word)] == word:
					result = result or travel(index + len(word))

			return result

		return travel(0)

def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    @lru_cache()
    def dp(s): return not s or any(dp(s[:-len(w)]) for w in wordDict if s[-len(w):] == w)
    return dp(s)

Traverse from the back.
Store the start index for which substring is found in wordDict.
Keep doing this till you reach 0th index.
def wordBreak(s, wordDict):
	n = len(s)
	wordDict = set(wordDict)
	isBreakable = False
	idx = [n]
	for i in range(n - 1, -1, -1):
		isBreakable = False
		for j in idx:
			if(s[i: j] in wordDict):
				isBreakable = True
				idx = [i] + idx
				break

	return isBreakable

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        elif not wordDict:
            return False

        n, cache, wordDict = len(s), [0], set(wordDict)

        for i in range(1, n + 1):  # here  i represents length
            if any(s[j:i] in wordDict for j in cache):
                cache.append(i)

        return cache[-1] == n

def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    d = [False] * len(s)
    
    for i in range(len(s)):
        for w in wordDict:

            if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                d[i] = True
                break
    return d[-1]