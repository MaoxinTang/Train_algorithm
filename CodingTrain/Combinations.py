class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def bt(prev):
            nonlocal ans
            if len(prev) == k:
                ans += prev,
                return
            for i in range(prev[-1] + 1, n + 1):
                bt(prev + [i])
                
        for j in range(1, n + 1):
            bt([j])
        return ans
in generator form:

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def bt(prev):
            if len(prev) == k:
                yield prev
            else:
                for i in range(prev[-1] + 1, n + 1):
                    yield from bt(prev + [i])
                    
        def main_gen():
            for j in range(1, n + 1):
                yield from bt([j])

        return list(main_gen())