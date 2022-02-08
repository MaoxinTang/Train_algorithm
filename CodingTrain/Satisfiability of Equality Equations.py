class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if x not in G:
                G[x] = x
                return x
            while G[x]!=x:
                x = G[x]
            return x
        
        def union(x,y):
            xp,yp = find(x), find(y)
            if xp!=yp:
                G[yp] = xp
        
        G = {}
        for e in equations:
            if e[1:3]=="==":
                union(e[0],e[3])
        for e in equations:
            if e[1:3]=="!=":
                if find(e[0])==find(e[3]):
                    return False
        return True