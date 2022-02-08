class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0
        
        def find_max(x, y):
            dic = {}
            for cur_x, cur_y in points:
                slope = "Inf" if y == cur_y else (cur_x - x) / (cur_y - y)
                if slope == "Inf":
                    dic[slope] = dic.get(slope, 0) + 1 ## need to offset 1 if we finally choose to use this "inf" vertical line (if we dont offset 1, we will count start point twice)
                else:
                    dic[slope] = dic.get(slope, 1) + 1  ## otherwise count start point in 
					
            return max(dic.values()) ## return cur_max
        
        for x, y in points: ## simply iterate through every point
            res = max(res, find_max(x, y))
        return res