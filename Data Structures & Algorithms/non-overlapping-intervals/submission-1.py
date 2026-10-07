class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # [[1,4][4,6][5,9][8,10]]
        # count = 0
        # res [1,5]
        # if overlap:
        # count + 1
        # if not overlap:
        #     append to res
        intervals.sort(key=lambda x:x[1])
        res = [intervals[0]]
        count = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start < res[-1][1]:
                count +=1
            else:
                res.append([start, end])
        return count
            