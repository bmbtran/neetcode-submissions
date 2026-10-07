class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        balance = 0
        for num in nums:
            if balance == 0: 
                candidate = num
            if num == candidate:
                balance +=1
            else:
                balance -=1
        return candidate
