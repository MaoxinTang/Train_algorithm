class Solution:
	def longestValidParentheses(self, s: str) -> int:
		maxL = 0
		stck = [-1]
		for i in range(len(s)):
			if s[i] == "(":
				stck.append(i)
			else:
				stck.pop()
				if len(stck) == 0:
					stck.append(i)
				else:
					maxL = max(maxL, i-stck[-1])
		return maxL