class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        l=sorted(heights)
        c=0
        for i in range(len(l)):
            if heights[i]!=l[i]:
                c+=1
        return c