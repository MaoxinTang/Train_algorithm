class Solution:
    """
    Find the array prefixes of runnning sums of w.
    Pick random number between 0 and sum(w)-1. Then binary search for the largest index of prefixes less    than or equal to random number.
    """

    def __init__(self, w: List[int]):
        prefix=0
        prefixes=[0]
        for weight in w:
            prefix+=weight
            prefixes.append(prefix)
        self.prefixes=prefixes

    def pickIndex(self) -> int:
        prefixes=self.prefixes
        rand_int=random.randint(0,prefixes[-1]-1)
        
        low,high=0,len(prefixes)-1
        while high-low>1:
            mid=low+(high-low)//2
            if prefixes[mid]>rand_int:
                high=mid-1
            elif prefixes[mid]<=rand_int:
                low=mid
        
        for i in range(high,low-1,-1):
            if prefixes[i]<=rand_int:
                return i