class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*(len(nums)+1)
        dp[0]=0
        dp[1]=nums[0]
        if n==0:
            return 0
        elif n==1:
            return nums[0]
        dp[2]=max(nums[0],nums[1])
        #dp[3]=max(dp[2],dp[1]+cost[3])
        for i in range(3,len(nums)+1):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i-1])
        print(dp)
        return dp[len(nums)]
        