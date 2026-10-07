class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        total = 0
        avg = 0
        count = 0
        for R in range(len(arr)):
            total += arr[R]
            if R-L+1 > k:
                total -= arr[L]
                avg = total /k
                L +=1
            if  R-L+1 == k:
                avg = total / k
                if avg >= threshold:
                   count +=1
        return count
        