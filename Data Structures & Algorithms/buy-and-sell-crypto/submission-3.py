class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #O(n^2) bruteforce solution:
        #have a maxProfit and generate every combination to find the maxProfit

        L = 0
        maxProfit = 0
        for R in range(len(prices)):
            while prices[R] < prices[L]:
                L = R
            maxProfit = max(maxProfit, prices[R] - prices[L])
        return maxProfit
            
