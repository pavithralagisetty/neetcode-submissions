class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        d=[(0,1),(1,0),(-1,0),(0,-1)]
        m=len(grid)
        n=len(grid[0])
        q=deque()
        c=0
        def bfs(x,y):
            q.append((x,y))
            grid[x][y]='0'
            while q:
                x,y=q.popleft()
                for dx,dy in d:
                    a=x+dx
                    b=y+dy
                    if 0<=a<m and 0<=b<n and grid[a][b]=='1':
                        q.append((a,b))
                        grid[a][b]='0'

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    c+=1
                    bfs(i,j)
        return c