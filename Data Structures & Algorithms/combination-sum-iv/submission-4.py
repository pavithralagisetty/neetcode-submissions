class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''c=0
        subset=[]
        res=[]
        nums.sort(reverse=True)
        s=0
        
        def dfs(s):
            if s==target:
                res.append(subset.copy())
                return
            if s>target:
                return
            for num in nums:
                subset.append(num)
                dfs(s+num)
                subset.pop()
        dfs(s)
        return len(res)'''
        dp=[0]*(target+1)
        dp[0]=1
        for a in range(1,target+1):
            for j in range(len(nums)):
                if (a-nums[j])>=0:
                    dp[a]+=dp[a-nums[j]]
        print(dp)
        return dp[target]