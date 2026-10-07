class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numsSet = set()
        L = 0
        for R in range( len(nums)):
            if R - L > k:
                numsSet.remove(nums[L])
                L += 1
            if nums[R] in numsSet:
                return True
            else:
                numsSet.add(nums[R])
        return False
