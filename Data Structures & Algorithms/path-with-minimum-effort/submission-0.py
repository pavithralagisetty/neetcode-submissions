class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m=len(heights)
        n=len(heights[0])
        heap=[]
        heapq.heappush(heap,(0,0,0))
        visit=set()
        di=[(0,1),(1,0),(-1,0),(0,-1)]
        while heap:
            d,x,y=heapq.heappop(heap)
            if (x,y) in visit:
                continue
            visit.add((x,y))
            if x==m-1 and y==n-1:
                return d
            for dx,dy in di:
                a=x+dx
                b=y+dy
                if 0<=a<m and 0<=b<n and (a,b) not in visit:
                    dist=max(d,abs(heights[a][b]-heights[x][y]))
                    
                    heapq.heappush(heap,(dist,a,b))