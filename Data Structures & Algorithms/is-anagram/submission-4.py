class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 2 maps
        # compare if 2 sets same then anagram time O(n) space O(n)
        #sort strings then compare O(nlogn) O(1)

        mapS = {}
        mapT = {}
        for c in s:
            if c in mapS:
                mapS[c] +=1
            else:
                mapS[c] = 1
        for c in t:
            if c in mapT:
                mapT[c] +=1
            else:
                mapT[c] = 1
        if mapS == mapT:
            return True
        else:
            return False