class Solution:
    def findComplement(self, num):
        i = 31
        while (num & 1 << i) == 0: 
            i -= 1
        while i >= 0:
            num ^= 1 << i
            i -= 1
        return num