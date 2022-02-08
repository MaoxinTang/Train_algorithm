class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0,1]
        for j in range(n and int(log2(n))):
            ans += [i+1 for i in ans] 
        return ans[:n+1]