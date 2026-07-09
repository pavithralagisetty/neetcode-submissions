class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        c=Counter(x)
        d=defaultdict(int)
        if len(c.keys())<3:
            return -1
        l=[]
        for i in range(len(x)):
            if d[x[i]]==0:
                d[x[i]]=y[i]
            elif d[x[i]]<y[i]:
                d[x[i]]=y[i]
        l=d.values()
        
        print(l)
        a=sorted(l, reverse=True)
        return sum(a[:3])
        
       
