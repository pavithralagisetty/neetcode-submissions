class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans=[]
        res=[]
        for l,r in points:
            ans.append(((l*l+r*r),l,r))
        ans.sort()
        for _,a,b in ans:
            if k>0:
                res.append((a,b))
            k-=1
        return res
