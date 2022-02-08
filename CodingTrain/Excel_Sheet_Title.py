class Solution:
    def convertToTitle(self, columnNumber):
        Num_to_alpha = {1: 'A',
                       2: 'B',
                       3: 'C',
                       4: 'D',
                       5: 'E',
                       6: 'F',
                       7: 'G',
                       8: 'H',
                       9: 'I',
                       10: 'J',
                       11: 'K',
                       12: 'L',
                       13: 'M',
                       14: 'N',
                       15: 'O',
                       16: 'P',
                       17: 'Q',
                       18: 'R',
                       19: 'S',
                       20: 'T',
                       21: 'U',
                       22: 'V',
                       23: 'W',
                       24: 'X',
                       25: 'Y',
                       26: 'Z'}
        if columnNumber in Num_to_alpha:
            return Num_to_alpha[columnNumber]
        ans = ""
        while columnNumber > 26:
            columnNumber, remainder = divmod(columnNumber, 26)
            if remainder == 0: 
                columnNumber -= 1 
                ans += Num_to_alpha[26]
            else: 
                ans += Num_to_alpha[remainder]
            
            if columnNumber <= 26:
                ans += Num_to_alpha[columnNumber]
        return ans[::-1]