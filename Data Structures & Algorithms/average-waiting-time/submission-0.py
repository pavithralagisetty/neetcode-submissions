class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        heap=[]
        p=0
        waittime=0
        for i,time in customers:
            heapq.heappush(heap,(i,time))
        while heap:
            
            i,time=heapq.heappop(heap)
            if p>i:
                p+=time
            else:
                p=i+time
            waittime+=p-i
        return waittime/len(customers)


        
    