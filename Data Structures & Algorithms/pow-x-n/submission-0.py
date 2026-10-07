class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = float(1)
        if n >0:
            while n:
                res = res * x
                n = n-1
            return res 
        else:
            while n < 0:
                # pow = abs(n)
                res = res *x
                n = n+1
            return 1/res