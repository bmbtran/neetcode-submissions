"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # 0-------------30
        # --5-10---------
        # ------15-20---
        # no conflict if startNext > endPrev
        intervals.sort(key=lambda i: i.start)
        curr = 0
        for interval in intervals:
            start = interval.start
            end = interval.end
            if start < curr:
                return False
            curr = end
        return True
