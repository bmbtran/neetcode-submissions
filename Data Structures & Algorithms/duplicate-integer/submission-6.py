class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #set - memory O(n)
        existed = set()
        for num in nums:
            if num in existed:
                return True
            else:
                existed.add(num)
        return False