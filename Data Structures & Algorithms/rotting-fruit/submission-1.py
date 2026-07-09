class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d=[(0,1),(1,0),(-1,0),(0,-1)]
        m= len(grid)
        n=len(grid[0])
        q=deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
        time=0
        while q:
            for _ in range(len(q)):
                print(q)
                x,y = q.popleft()
                for dx,dy in d:
                    a=x+dx
                    b=y+dy
                    if 0<=a<m and 0<=b<n and grid[a][b]==1:
                        q.append((a,b))
                        grid[a][b]=2

            time+=1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        if grid[0][0]==0:
            return 0
        return time-1
