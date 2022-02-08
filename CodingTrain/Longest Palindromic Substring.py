class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Manacher's Algorithm
        
        # First, insert * into s. e.g. 'aab' -> '*a*a*b*'
        ns = '*'
        for i in s:
            ns += i
            ns += '*'
        
		# Initialize a list to record the longest palindromic substring of every character of the new string if we regard the character as center
		# 'rightmost' is used to record the rightmost character which is in some palindromic substring whose center is 'center'
        center, rightmost = 0, 0
        lps = [0] * len(ns)
        
		
        for i in range(len(ns)):
            
			# if i is to the right of the rightmost character, initialize lps[i] as 0, otherwise we can refer it by its reflection w.r.t 'center'
            if i > rightmost:
                lps[i] = 0
            else:
				# 'mirror' is the refection of ns[i] w.r.t 'center'
                mirror = 2 * center - i
                lps[i] = min(lps[mirror], rightmost-i)
                
            try:
                while ns[i+lps[i]+1] == ns[i-lps[i]-1]:
                    lps[i] += 1
            except:
                pass
            
			# Update center and rightmost
            if lps[i] + i > rightmost:
                center = i
                rightmost = lps[i] + i
                
        lpsIndex, lpsRange = lps.index(max(lps)), max(lps)
        temp = ''.join(ns[lpsIndex-lpsRange:lpsIndex+lpsRange])
        
        return temp.replace('*', '')