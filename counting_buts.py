class Solution(object):
    def countBits(self, n):
        l=[]    
        for i in range(n+1):
            b=bin(i)[2:]
            s=sum(1 for j in str(b) if int(j)==1) 
            l.append(s)
        return l
