class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        
        ret = [1]
        heap = []
        
        for prime in primes:
            heapq.heappush(heap, (prime, 0, prime))
        
        while len(ret) < n:
            nex, idx, prime = heapq.heappop(heap)
            ret.append(nex)
            idx += 1
            heapq.heappush(heap, (ret[idx] * prime, idx, prime))

            if ret[-1] == ret[-2]:
                ret.pop()
            
        return ret[-1]