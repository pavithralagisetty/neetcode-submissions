class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        c=0
        parent=[x for x in range(n)]
        rank=[0]*n
        s=set()
        def union(dx,dy):
            x=find(dx)
            y=find(dy)
            if x!=y:
                if rank[x]<rank[y]:
                    parent[x]=y
                elif rank[y]<rank[x]:
                    parent[y]=parent[x]
                else:
                    parent[y]=parent[x]
                    rank[x]+=1
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        for u,v in edges:
            union(u,v)        
        for i in range(n):
            s.add(find(i))
        return len(s)



    