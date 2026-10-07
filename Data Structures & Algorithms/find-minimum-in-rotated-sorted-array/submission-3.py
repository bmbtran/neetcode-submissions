class Solution:
    #[6,1,2,3,4,5]
    #find pivot point
    #compare to rightmost element, if larger then belong to large section, we wanna go to small section
    #, else small section, then look to the left to find min of that section
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) -1
        while L <= R:
            mid = (L+R) //2
            if nums[mid] > nums[R]:
                L = mid +1
            elif nums[mid] < nums[R]:
                R = mid
            else:
                return nums[R]
