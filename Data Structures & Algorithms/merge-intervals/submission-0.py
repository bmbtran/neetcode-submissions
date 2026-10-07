class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #first sort 
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            #non overlap
            if curr[0] > res[-1][1]:
                res.append(curr)
            #overlap
            else:
                curr = [min(res[-1][0], curr[0]), max(res[-1][1], curr[1])]
            res[-1] = curr
        return res