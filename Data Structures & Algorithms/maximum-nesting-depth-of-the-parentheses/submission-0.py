class Solution:
    def maxDepth(self, s: str) -> int:
        c=0
        maxc=0
        for i in range(len(s)):
            if s[i]=='(':
                c+=1
            if s[i]==')':
                c-=1
            maxc=max(c,maxc)
        return maxc