class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #use set cuz we want fast lookup
        nums = set(nums)
        maxLength = 0
        num = 0
        for num in nums:
            if (num-1) not in nums:
                length = 1
                while num + length in nums:
                    length += 1
                maxLength = max(maxLength, length)
        return maxLength
