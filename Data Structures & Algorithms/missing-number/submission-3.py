class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #brute force
        #for num in range (0, n+1):
        #if num not in nums:
        # return num
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res

        #O(n^2) because "in" list is O(n)
        #O(n) - O(n) because searching set 
