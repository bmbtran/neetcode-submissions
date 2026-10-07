class Solution:
    def countBits(self, n: int) -> List[int]:
        #[0,1,2,3,4]
        #loop through that arr, for each element, count num of 1 bits
        #then append to res [] the num of bit 
        #logic for counting num of 1 bits:
        #num (int)
        #32 bits. 0000...0000, 0....0001, 0....0010 & 1 
        res = []
        for num in range(n+1):
            count = 0
            while num > 0:
                if num & 1 == 1:
                    count +=1
                num >>=1
            res.append(count)
        return res

