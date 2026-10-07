class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # map = {num: index}
        # if diff in retun [index and currindex]
        # O(n) space and O(n) time

        map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map:
                return [map[diff], i]
            map[nums[i]] = i
        
