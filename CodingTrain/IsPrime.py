class Solution:
    def countPrimes(self, n: int) -> int:
        
        IsPrime = [True] * (n + 1)
        for i in range(2, int(n ** 0.5) + 1):
            if IsPrime[i]:
                for j in range(i * i, n + 1, i):
                    IsPrime[j] = False
        return len([x for x in range(2, n) if IsPrime[x]])