class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #1- indexed -> +1 when returning
        #sorted arr -> 2 pointers
        L, R = 0, len(numbers) -1
        while L < R:
            if numbers[R] + numbers[L] > target:
                R -= 1
            elif numbers[R] + numbers[L] < target:
                L += 1
            else:
                return [L+1, R+1]