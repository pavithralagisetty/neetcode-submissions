class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}
        s=set()
        c=0
        minH=[[0,0]]
        for i in range(N):
            for j in range(i + 1, N):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        print(adj)
        while len(s)!=N:
            cost,n=heapq.heappop(minH)
            if n not in s:
                s.add(n)
                c+=cost
                for i,j in adj[n]:
                    heapq.heappush(minH,[i,j])
        return c