class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        ans = [0] * len(temperatures)
        s = deque()
        s.append((temperatures[0], 0))
        
        for i in range(1, len(temperatures)):
            curr_temp = temperatures[i]
            while(s):
                temp, idx = s.pop()
                if temp < curr_temp:
                    ans[idx] = i-idx
                else:
                    s.append((temp, idx))
                    break
            s.append((curr_temp, i))
        return ans