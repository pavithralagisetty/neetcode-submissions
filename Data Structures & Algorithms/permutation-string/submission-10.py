class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=len(s1)
        d=Counter(s1)
        for i in range(len(s2)):
            
            if i+r<len(s2)+1:
                print(s2[i:i+r])
                if d==Counter(s2[i:i+r]):
                    return True
        return False

