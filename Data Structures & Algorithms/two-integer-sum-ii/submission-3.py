class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) -1
        while L < R:
            sumNums = numbers[L] + numbers[R]
            if sumNums > target:
                R -=1
            elif sumNums < target:
                L +=1
            else:
                return [L+1, R+1]