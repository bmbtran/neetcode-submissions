class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(j, path):
            res.append(path.copy())
            for i in range(j, len(nums)):
                if i>j and nums[i] == nums[i-1]:
                    continue
        
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()



        dfs(0, [])
        return res