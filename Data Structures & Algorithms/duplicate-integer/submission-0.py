class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existed = []
        for i in range(len(nums)):
            if nums[i] in existed: 
                return True
            else:
                existed.append(nums[i])
        return False