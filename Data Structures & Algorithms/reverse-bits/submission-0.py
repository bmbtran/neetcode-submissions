class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for i in range(32):
            output <<= 1 #shift left to make room
            output |= n & 1 
            n >>= 1 #shift right to drop the bit we just added to reverse
        return output
