class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        d=[(0,1),(1,0),(-1,0),(0,-1)]
        m=len(grid)
        n=len(grid[0])
        q=deque()
        maxarea=0
        def bfs(x,y):
            area=0
            nonlocal maxarea
            q.append((x,y))
            while q:
                
                a,b=q.popleft()
                grid[a][b]=0
                area+=1
                for dx,dy in d:
                    r=a+dx
                    c=b+dy
                    if 0<=r<m and 0<=c<n and grid[r][c]==1:
                        
                        grid[r][c]=0
                        q.append((r,c))
            maxarea=max(maxarea,area)



        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    bfs(i,j)
        return maxarea