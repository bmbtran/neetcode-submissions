class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existed = set()
        for i in range(len(nums)):
            if nums[i] in existed:
                return True
            else:
                existed.add(nums[i])
        return False