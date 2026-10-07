class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #no duplicates
        subSets, curSet = [], []
        def helper(i):
            if i >= len(nums):
                subSets.append(curSet.copy())
                return 
            #decision if we include i
            curSet.append(nums[i])
            helper(i+1)
            curSet.pop()
            #decision if we dont include i
            helper(i+1)
        helper(0)
        return subSets
    

