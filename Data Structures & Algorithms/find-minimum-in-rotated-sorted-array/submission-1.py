class Solution:
    #[6,1,2,3,4,5]

    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) -1
        while L < R:
            mid = (L+R) //2 #5
            if nums[mid] >= nums[R]:
                L = mid +1
            else:
                R = mid
        return nums[L]