class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1 not in num_set:
                current = num
                consecutive = 1
                while current + 1 in num_set:
                    current += 1
                    consecutive += 1
                longest = max(longest, consecutive)
        return longest
