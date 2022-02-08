from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        freq = [(-v, k) for k, v in c.items() ]
        heapq.heapify(freq)
           
        return [heapq.heappop(freq)[1] for _ in range(k) ]