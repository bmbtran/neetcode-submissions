class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #increment last element by 1
        #handle 10 -> carry over.
        #for i in range(len(digits) -1 , -1, -1):
        #2 cases:
        #if 9 -> 0 and carry 1 over
        #normal.
        #[9,7,9]
        for i in range(len(digits) -1, -1, -1):
            if digits[i] != 9:
                digits[i] +=1
                return digits
            else:
                digits[i] = 0
        return [1] + digits

