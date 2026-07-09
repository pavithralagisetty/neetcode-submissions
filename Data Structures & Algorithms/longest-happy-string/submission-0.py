class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap=[]
        l=[(-a,'a'),(-b,'b'),(-c,'c')]
        res=""
        for count,ch in l:
            if count!=0:
                heapq.heappush(heap,(count,ch))
        while heap:
            count,ch=heapq.heappop(heap)
            if count==0:
                continue
            elif len(res)>1 and res[-1]==res[-2]==ch:
                if not heap:
                    break
                count2,ch2=heapq.heappop(heap)
                res+=ch2
                count2+=1
                if count2<0:
                    heapq.heappush(heap,(count2,ch2))
                heapq.heappush(heap,(count,ch))
                continue
            res+=ch
            count+=1
            if count<0:
                heapq.heappush(heap,(count,ch))
        return res
