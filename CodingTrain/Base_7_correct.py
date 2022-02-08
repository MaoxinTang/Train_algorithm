class Solution:
    def convertToBase7(self, num: int) -> str:
        
        if -6 <= num <= 6:
            return str(num)
        
        neg = True if num < 0 else False
        
        num = abs(num)
        
        highest_seven = 0
        
        while num / (7**highest_seven) >= 1:
            highest_seven += 1
        highest_seven -= 1
        
        r = ""
        while highest_seven >= 0:
            m = 7**highest_seven
            d = num // m
            if d > 0:
                num -= m*d
            r += str(d)
            highest_seven -= 1
        
        return '-'+r if neg else r