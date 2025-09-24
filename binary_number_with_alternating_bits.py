class Solution(object):
    def hasAlternatingBits(self, n):
        b=bin(n)[2:]
        t=True
        for i in range(0,len(str(b))-1):
            if b[i]==b[i+1]:
                t=False
                break
        return t
