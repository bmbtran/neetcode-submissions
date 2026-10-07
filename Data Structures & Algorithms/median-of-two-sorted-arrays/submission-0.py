class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #median: if odd # -> value [len // 2 +1]
        #if even # -> avg(value[len//2], value[len//2+1])
        #binary search
        combined = nums1 + nums2 #O(n)
        combined.sort()
        L, R = 0, len(combined) -1 
        res = 0
        if len(combined) % 2 == 0:
            res = float((combined[R//2] + combined[R//2 + 1]) /2)
        else:
            res = float(combined[R//2])
        return res




        #bin search solution
        #

