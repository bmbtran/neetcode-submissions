class Solution:

    def encode(self, strs: List[str]) -> str:
        self.encoded = ''
        for s in strs:
            self.encoded += str(len(s)) + '%' + s
        return self.encoded
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(self.encoded):
            n = ''
            while self.encoded[i] != '%':
                n += self.encoded[i]
                i +=1
                continue
            n = int(n)
            res.append(self.encoded[i+1:i+1+n])
            i = i+1+n
        #res add next n number of chars
        return res



# 24%Hello1%%2%452%World

