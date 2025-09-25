class Solution(object):
    def evenOddBit(self, n):
        b=(bin(n)[2:])[::-1]
        e=sum(1 for i in range(0,len(b)) if i%2==0 and b[i]=='1')
        o=sum(1 for i in range(0,len(b)) if i%2!=0 and b[i]=='1')
        return [e,o]
