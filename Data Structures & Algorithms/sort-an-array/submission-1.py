class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        l=[]
        for i in range(-50000,50001):
            while i in c and c[i]>0:
                l.append(i)
                c[i]-=1
        return l