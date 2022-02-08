class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        value = [0]*n
        ans = 0
        for i in range(n):
            for j in words[i]:
                value[i] |= 1<<(ord(j)-97)
        for i in range(n):
            for j in range(i+1,n):
                if value[i] & value[j] == 0:
                    ans = max(ans,len(words[i])*len(words[j]))
        return ans