class Solution:
    def jump(self, nums: List[int]) -> int:
        L, R = 0, 0 #R: maxreachable
        maxReach = 0
        count = 0
        while R < len(nums) -1:
            for i in range(L, R+1):
                maxReach = max(maxReach, i + nums[i])
            L = R + 1
            R = maxReach        
            count +=1        
        return count        

                