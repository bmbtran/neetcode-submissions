class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffToIndex = {}
        res = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diffToIndex:
                res.append(diffToIndex[diff])
                res.append(i)
                return res
            else:
                diffToIndex[nums[i]] = i