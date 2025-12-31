class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0
        res = 0
        for i in range(32):
            res = res << 1
            bit = n & 1
            res = res + bit
            n = n >> 1
            

        return res