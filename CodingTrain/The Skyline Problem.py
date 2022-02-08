class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        outline = []
        
        for left, right, height in buildings:
            outline.append([left, -height, 'start'])
			# the "-" before height for left position is due to the corner cases 
			# because the algorithm is input-order-sensitive 
			# later in priority queue, we need to remove the "-"
            outline.append([right, height, 'end'])
            
        outline.sort()
        ans, pq, prev = [], [0], 0
        
        for position, height, ty in outline:
            if ty == 'start':
                bisect.insort_right(pq, -height)  
				# we can use both insort_right or insort_left
				# both are AC 
            else:
                index = bisect.bisect_left(pq, height) 
				# avoid the out of range due to bisect_right/bisect
                pq.pop(index)
            
            curr_height = pq[-1]   #pq is a non decreasing pq
            
            if prev == curr_height:
			# if outline remains the same height, continure without any output
                continue
            else:
			# report the change of height in output
                ans.append([position, curr_height])
                prev = curr_height
                
        return ans