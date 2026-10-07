class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #use stack?
        #use set? 
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            elif num in seen:
                seen.remove(num)
        digit = seen.pop()
        return digit