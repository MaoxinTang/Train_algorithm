class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        provinces = set()
        provs = 0
        graph = {}
        
        def dfs(key,s):
            if key not in s:
                s.add(key)
                provinces.add(key)
                for node in graph.get(key):
                    dfs(node,s)
            
        for index,connection in enumerate(isConnected):
            if graph.get(index) is None:
                graph[index] = []
            for nindex,item in enumerate(connection):
                if nindex != index and item == 1:
                    graph[index].append(nindex)
        
        for key in graph:
            if key not in provinces:
                provinces.add(key)
                provs += 1
            dfs(key,set())
        
        return provs