class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #len(piles) < h
        #binary search guess k over [1...11]
        #ex: k = 6, hours = 12 when h = 9
        low, high = 1, max(piles) # [1,2,3,4]
        res = 0
        while low <= high:
            hours = 0
            mid = (high + low) //2 #k=
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/mid)
            if hours <= h:
                high = mid -1
                res = mid
            else:
                low = mid +1
        return res


