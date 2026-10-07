class Solution:
    def canJump(self, nums: List[int]) -> bool:
#         max reachable: 
#         index + val 
#         1
#         3
#         as long as within < maxreachable
# nums = [1,2,2,0, 0, 1,1]
#         if at maxReachable index and cant reach more:
#             return false

#         3
#         3
        maxReachable = 0
        for i in range(len(nums)):
            if i > maxReachable:
                return False
            maxReachable = max(maxReachable, i + nums[i])
        return True

