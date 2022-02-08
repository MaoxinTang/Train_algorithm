class Solution(object):
    """dfs-backtracking"""
    
    def findItinerary(self, tickets):
        adj = collections.defaultdict(list)
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
            
        res = ["JFK"]
        
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            
            tmp = adj[src].copy()
            for i, v in enumerate(tmp):
                adj[src].pop(i)
                res.append(v)
                
                if dfs(v):
                    return True
                adj[src].insert(i, v)
                res.pop()
            return False
        
        dfs("JFK")
        return res