class Solution(object):
    def reverseBits(self, n):
        rev=bin(n)[2:].zfill(32)
        b=int(rev[::-1],2)
        return b
