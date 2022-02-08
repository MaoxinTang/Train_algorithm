class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.freq = defaultdict(int)
        self.minheap = []
        self.maxheap = []
        

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        self.freq[key] += 1
        heappush(self.minheap, [self.freq[key], key])
        heappush(self.maxheap, [-self.freq[key], key])

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        self.freq[key] -= 1
        heappush(self.minheap, [self.freq[key], key])
        heappush(self.maxheap, [-self.freq[key], key])

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        #print(self.freq, self.maxheap)
        while self.maxheap:
            topFreq, topVal = self.maxheap[0]
            if topFreq == 0:
                heappop(self.maxheap)
                continue
                
            if self.freq[topVal] == -topFreq:
                return topVal
            heappop(self.maxheap)
            
        return ''

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        while self.minheap:
            topFreq, topVal = self.minheap[0]
            if topFreq == 0:
                heappop(self.minheap)
                continue
                
            if self.freq[topVal] == topFreq:
                return topVal
            heappop(self.minheap)
            
        return ''
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()