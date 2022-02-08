class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        nonZeros, answer = x^y, 0
        
        while nonZeros > 0:
            nonZeros = nonZeros & (nonZeros-1)
            answer += 1
            
        return answer      