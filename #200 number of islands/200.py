class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        m, n, cnt = len(grid), len(grid[0]), 0
        if m <= 0 or n <= 0: return 0
        cgrid = [ [ i*n+j if grid[i][j] == "1" else -1 for j in range(n) ] for i in range(m)]

        def getIndex(product):
            i = product/n
            j = product - i*n
            return i,j
        
        def find(tar):
            i,j = getIndex(tar)
            if tar < 0: return -1
            t = cgrid[i][j]
            if t == tar: return tar
            return find(t)

        def union(grid):
            for i in range(1, m):
                if grid[i][0] >= 0:
                    if grid[i-1][0] >= 0: grid[i][0] = grid[i-1][0]
            for j in range(1, n):
                if grid[0][j] >= 0:
                    if grid[0][j-1] >= 0: grid[0][j] = grid[0][j-1]
  
            for i in range(1,m):
                for j in range(1,n):
                    if cgrid[i][j] < 0: continue
                    t1 = find(cgrid[i][j-1])
                    t2 = find(cgrid[i-1][j])
                    if t1 >= 0 and t2 >= 0:
                        i2,j2 = getIndex(t2)
                        cgrid[i][j] = cgrid[i2][j2] = t1
                    elif t1 >= 0: cgrid[i][j] = t1
                    elif t2 >= 0: cgrid[i][j] = t2
            return grid

        cgrid = union(cgrid)
    
        for i in range(m):
            for j in range(n):
                if cgrid[i][j] == n*i+j: cnt = cnt + 1
        return cnt