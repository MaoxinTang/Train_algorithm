class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        temp = -1
        while n > 0:
            digit = n&1
            if digit == temp:
                return False
            n = n>>1
            temp = digit
            
        return True
        