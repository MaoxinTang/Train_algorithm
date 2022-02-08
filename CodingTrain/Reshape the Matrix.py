from itertools import chain

class Solution(object):
    
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        original = list(chain.from_iterable(mat)) # sum(mat,[]) is faster but not recommened in Python docs
        
        N = len(original)
        
        if r*c != N:
            return mat
        
        res = []
        for i in range(0, N, c):
            res.append(original[i:i+c])
        
        return res