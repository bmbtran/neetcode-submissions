class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 3 bin search passes?
        # 1 to find min
        # 1 search on left side
        # 1 search on right side
        L, R = 0, len(nums) -1
        minI = 0
        if nums[L] > nums[R]:
            while L < R:
                mid = (L+R) //2
                if nums[mid] > nums[R]:
                    L = mid +1
                else:
                    R = mid
            minI = L
        if target > nums[-1]:
            L, R = 0, minI -1
            while L <= R:
                mid = (L+R) //2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    L = mid +1
                else:
                    R = mid -1
        else:
            L, R = minI, len(nums) -1
            while L <= R:
                mid = (L+R) //2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    L = mid +1
                else:
                    R = mid -1
        return -1
        
            
        

        

        return -1

