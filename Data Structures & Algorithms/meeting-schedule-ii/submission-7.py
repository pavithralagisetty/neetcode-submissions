"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap=[]
        intervals.sort(key=lambda x:x.start)
        for i in intervals:
            start=i.start
            end=i.end
            if heap and start>=heap[0]:
                heapq.heappop(heap)
                
            heapq.heappush(heap,end)
        return len(heap)