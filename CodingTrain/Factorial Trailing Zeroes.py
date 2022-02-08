class Solution:
    def trailingZeroes(self, n: int) -> int:
        def noOfFactors(num, div):
            noOfFactors = 0
            while num%div == 0:
                num = num // div
                noOfFactors += 1
            return noOfFactors, num
                
        tens = 0
        twos = 0
        fives = 0
        for i in range(1, n+1):
            ct, i = noOfFactors(i, 10)
            tens += ct
            ct, i = noOfFactors(i, 2)
            twos += ct
            ct, i = noOfFactors(i, 5)
            fives += ct
                
        return tens + min(twos, fives)