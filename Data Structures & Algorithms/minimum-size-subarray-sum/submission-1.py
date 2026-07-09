class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        c=0
        minlen=float('inf')
        
        for r in range(len(nums)):
            c+=nums[r]
            while c>=target:
                minlen=min(minlen,r-l+1)
                c-=nums[l]
                l+=1
        if minlen==float('inf'):
            return 0
        return minlen
            
