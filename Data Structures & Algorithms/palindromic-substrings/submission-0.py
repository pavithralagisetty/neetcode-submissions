class Solution:
    def countSubstrings(self, s: str) -> int:
        c=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                st=s[i:j+1]
                if (s[i:j+1]==st[::-1]):
                    c+=1
        return c