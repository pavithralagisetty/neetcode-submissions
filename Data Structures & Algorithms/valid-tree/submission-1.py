class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent=[x for x in range(n)]
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            
            x=find(x)
            y=find(y)
            if x==y:
                return False
            parent[x]=y
        for u,v in edges:
            if union(u,v)==False:
                return False
        a=set()
        for i in range(n):
            a.add(find(i))
        if len(a)==1:
            return True
        
        return False
        
