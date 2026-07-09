class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        d=defaultdict(int)
        maxi = 0
        for r in range(len(s)):
            d[s[r]]+=1
            while d[s[r]]>1:
                
                d[s[l]]-=1
                l+=1
            
            maxi=max(maxi,r-l+1)
        return maxi
            