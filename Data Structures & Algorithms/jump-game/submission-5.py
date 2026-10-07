class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i =0
        maxReachable = 0
        while i < len(nums):
            if i > maxReachable:
                return False
            maxReachable = max(maxReachable, i + nums[i])
            i+=1
        if maxReachable >= len(nums) -1:
                return True

