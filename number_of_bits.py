class Solution(object):
    def hammingWeight(self, n):
        b=str(bin(n)[2:])
        s=b.replace("0","")
        return len(s)
        
