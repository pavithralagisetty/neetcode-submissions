class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        v='aeiou'
        l=[]
        for word in words:
            if word[0] in v and word[-1] in v:
                l.append(1)
            else:
                l.append(0)
        res=[]
        for l1,r1 in queries:
            res.append(sum(l[l1:r1+1]))
        
        return res