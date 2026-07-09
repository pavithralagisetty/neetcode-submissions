class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        d=defaultdict(int)
        maxi=0
        for r in range(len(fruits)):
            if fruits[r] in d:
                d[fruits[r]]+=1
            elif len(d.values())<2:
                d[fruits[r]]=1
            else:
                d[fruits[r]]+=1
                while len(d.keys())>2:
                    d[fruits[l]]-=1
                    
                    if d[fruits[l]]==0:
                        del d[fruits[l]]
                    l+=1
                
                
            maxi=max(maxi,r-l+1)
        return maxi