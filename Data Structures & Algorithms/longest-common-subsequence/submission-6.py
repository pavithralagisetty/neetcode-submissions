class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)

        dp=[[0]*(m+1) for _ in range(n+1)]
        print(dp)
        for i in range(n):
            for j in range(m):
                if text1[j]==text2[i]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        print(dp)
        return dp[n-1][m-1]