class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        l=heights[-1]
        ans=[]
        ans.append(len(heights)-1)
        for i in range(len(heights)-2,-1,-1):
            if heights[i]>l:
                ans.append(i)
                l=heights[i]
        return sorted(ans)
