class Solution(object):
    def countDigits(self, num):
        s=str(num)     
        c=0
        c=sum(1 for i in s if int(s)%int(i)==0)
        return c
