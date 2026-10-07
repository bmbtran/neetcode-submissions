class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + '%' + s
        return encoded
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            n = ''
            while s[i] != '%':
                n += s[i]
                i +=1
                continue
            n = int(n)
            res.append(s[i+1:i+1+n])
            i = i+1+n
        #res add next n number of chars
        return res



# 24%Hello1%%2%452%World

