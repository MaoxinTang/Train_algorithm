class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        nRows = len(heights)
        nCols = len(heights[0])
        
        lRow = nRows-1
        lCol = nCols-1
        
        reachPacific = []
        reachAtlantic = []
        for i in range(nRows):
            reachPacific.append([False]*nCols)
            reachAtlantic.append([False]*nCols)
        
        def dfs(reachOcean, i, j, prevH = 0):
            # check i and j
            if i>lRow or j>lCol or i<0 or j<0:
                return
            
            # if already know ocean can be reached from here
            if reachOcean[i][j]:
                return
            
            # check if ocean can be reached from here
            h = heights[i][j]
            if h<prevH:
                return
            reachOcean[i][j] = True
            
            # move to adjacent squares
            dfs(reachOcean, i+1, j, h)
            dfs(reachOcean, i-1, j, h)
            dfs(reachOcean, i, j+1, h)
            dfs(reachOcean, i, j-1, h)
        
        # try to reach each square on
        # pacific left coast
        for i in range(nRows):
            dfs(reachPacific, i, 0)
        
        # try to reach each square on
        # pacific top coast
        for j in range(nCols):
            dfs(reachPacific, 0, j)

        # try to reach each square on
        # atlantic right coast
        for i in range(nRows):
            dfs(reachAtlantic, i, lCol)
        
        # try to reach each square on
        # atlantic bottom coast
        for j in range(nCols):
            dfs(reachAtlantic, lRow, j)
            
        res = []
        for i in range(nRows):
            for j in range(nCols):
                if reachAtlantic[i][j] and reachPacific[i][j]:
                    res.append([i,j])
        return res