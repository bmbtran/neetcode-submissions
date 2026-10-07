class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #naive: 
        #o nlogn: sort both and if equal then same
        #o(n) and o(1) space: [0] *26 
        sArr = [0] *26
        tArr = [0] *26

        for i in range(len(s)):
            ind = ord(s[i]) - ord('a')
            sArr[ind] +=1
        for i in range(len(t)):
            ind = ord(t[i]) - ord('a')
            tArr[ind] +=1
        return sArr == tArr