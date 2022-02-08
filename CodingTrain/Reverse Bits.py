class Solution:
    def reverseBits(self, n):
        res = 0
        pos = 31
        while pos >= 0:
            if n&(1<<(31-pos)):
                res = res | 1<<pos
            pos -=1
        return res