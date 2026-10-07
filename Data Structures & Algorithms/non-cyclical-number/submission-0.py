class Solution:
    def isHappy(self, n: int) -> bool:
        #cycle detection -> fast and slow pointers on linked list
        slow, fast = n, self.sumOfSquares(n)
        while slow != fast:
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)
        return True if fast == 1 else False


    def sumOfSquares(self, n):
        total = 0 
        while n:
            digit = n % 10
            total += digit **2
            n = n // 10
        return total


