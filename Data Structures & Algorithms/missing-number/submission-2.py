class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #brute force
        #for num in range (0, n+1):
        #if num not in nums:
        # return num
        nums_set = set(nums)
        for num in range(len(nums_set) +1):
            if num not in nums_set:
                return num

        #O(n^2) because in is O(n)