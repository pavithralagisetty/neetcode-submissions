class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        l=[]
        for n,f,t in trips:
            l.append((f,n))
            l.append((t,-n))
        l.sort()
        maxi=0
        for x,y in l:
            maxi+=y
            if maxi>capacity:
                return False
        return True

