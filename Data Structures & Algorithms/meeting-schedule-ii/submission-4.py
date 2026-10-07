"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # (5,10)(15,20)(0,40)
        import heapq
        intervals.sort(key=lambda x:x.start)
        minHeap = []
        for interval in intervals:
            #reuse the room by popping -> updating the room end time
            if minHeap and interval.start >= minHeap[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, interval.end)
        return len(minHeap)
            
        

