class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #bin search range
        #can only do this cuz its sorted
        L, R = 1, max(piles)-1
        res = max(piles)
        # piles[i]/h
        while L <= R:
            mid = (L+R)//2
            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile/mid)
            if totalHours <= h:
                res = mid
                R = mid -1
            elif totalHours > h:
                L = mid +1
        return res
            