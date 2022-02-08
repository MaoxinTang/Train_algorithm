class Solution:
    def frequencySort(self, s: str) -> str:
        return reduce(lambda a, b: a + b[1]*b[0], Counter(s).most_common(), '')

class Solution:
    def frequencySort(self, s: str) -> str:
        counter=Counter(s)
        res=""
        for char,count in sorted(counter.items(),key=lambda item:item[1],reverse=True):
            res+=(char*count)
        return res

class Solution:
    def frequencySort(self, s: str) -> str:
        
        c = collections.Counter(s)
        
        res = []
        
        for string, times in c.items():
            res.append(string * times)
        
        def magic(i):
            return len(i)
        
        res.sort(reverse = True, key = magic)
        
        return "".join(res)