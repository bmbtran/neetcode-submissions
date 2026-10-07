class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # keep expanding 
        # maxTotal = 
        # keep a total
        # if sum < 0 : move start to next pointer
        
        maxTotal = nums[0]
        i =0
        total = 0
        while i < len(nums):
            total += nums[i]
            maxTotal = max(total, maxTotal)
            if total <0:
                total = 0

            i+=1

        return maxTotal
