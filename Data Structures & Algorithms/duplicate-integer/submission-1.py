class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existed = set()
        for i in nums:
            if i in existed: 
                return True
            else:
                existed.add(i)
        return False