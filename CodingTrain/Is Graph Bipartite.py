class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n=len(graph)
        
        color=[0]*n
        
        for i in range(n):
            
            if color[i]==0 and not self.validcolor(graph,color,1,i):
                return False
        return True
    
    def validcolor(self,graph,color,blue,i):
        
        if color[i]!=0:
            return color[i]==blue
        
        color[i]=blue
        
        for neighbour in graph[i]:
            if not self.validcolor(graph,color,-blue,neighbour):
                return False
        
        return True