class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=len(s1)
        if len(s1) > len(s2):
            return False
        d1,d2=defaultdict(int),defaultdict(int)
        for i in range(len(s1)):
            d1[s1[i]]+=1
            d2[s2[i]]+=1
        if d1==d2:
                return True
        while r<len(s2):
            
            d2[s2[r]]+=1
            
            d2[s2[l]]-=1
        
            if d2[s2[l]]==0:
                del d2[s2[l]]
            
            if d1==d2:
                return True
            r+=1
            l+=1
        return False
