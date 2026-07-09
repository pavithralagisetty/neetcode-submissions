class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        c=0
        parent=[x for x in range(n)]
        s=set()
        def union(dx,dy):
            x=find(dx)
            y=find(dy)
            if x!=y:
                parent[y]=x
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        for u,v in edges:
            union(u,v)
        print(parent)
        
        for i in range(n):
            s.add(find(i))
        return len(s)



    