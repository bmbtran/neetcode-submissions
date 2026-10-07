class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #if newInterval.start < interval.end:
        #interval.end = newInterval.end
        # [1,5]
        res = []
        for i in range(len(intervals)):
            interval = intervals[i]
            if newInterval[1] < interval[0] :
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > interval[1]:
                res.append(interval)
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])] 
        res.append(newInterval)
        return res