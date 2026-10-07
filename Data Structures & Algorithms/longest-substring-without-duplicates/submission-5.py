class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        L= 0
        maxL = 0
        curSet = set()
        for R in range(len(s)):
            while s[R] in curSet:
                curSet.remove(s[L])
                L +=1

            curSet.add(s[R])
            maxL = max(maxL, R-L+1)
        return maxL
