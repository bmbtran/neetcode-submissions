class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #brute force
        #for num in range (0, n+1):
        #if num not in nums:
        # return num
        for num in range(len(nums) +1):
            if num not in nums:
                return num