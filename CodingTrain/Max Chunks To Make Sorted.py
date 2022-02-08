class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n=len(arr)
        curr=0
        sum1=0
        chunks=0
        for i in range(n):
            curr+=(arr[i]+1)
            sum1+=(i+1)
            if curr==sum1:
                chunks+=1
        return chunks