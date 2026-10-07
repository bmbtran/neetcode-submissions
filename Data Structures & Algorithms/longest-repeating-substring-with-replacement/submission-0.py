class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        L = 0
        length = 0
        for R in range(len(s)):
            #expand
            count[s[R]] = 1 + count.get(s[R], 0)
            #shrink
            while (R-L+1) - max(count.values()) > k:
                count[s[L]] -= 1
                L +=1
            #update
            length = max(length, R-L+1)
        return length