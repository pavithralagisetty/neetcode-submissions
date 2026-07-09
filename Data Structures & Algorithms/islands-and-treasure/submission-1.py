class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m=len(grid)
        n=len(grid[0])
        q=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append((i,j))
        while q:
            x,y=q.popleft()
            if x+1<m and grid[x+1][y]==2147483647:
                grid[x+1][y]=grid[x][y]+1
                q.append((x+1,y))
            if y+1<n and grid[x][y+1]==2147483647:
                grid[x][y+1]=grid[x][y]+1
                q.append((x,y+1))
            if x-1>=0 and grid[x-1][y]==2147483647:
                grid[x-1][y]=grid[x][y]+1
                q.append((x-1,y))
            if y-1>=0 and grid[x][y-1]==2147483647:
                grid[x][y-1]=grid[x][y]+1
                q.append((x,y-1))
