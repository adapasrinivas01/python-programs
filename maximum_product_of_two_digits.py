class Solution(object):
    def maxProduct(self, n):
        m=0
        s=str(n)
        for i in range(len(s)):
            for j in range(len(s)):
                if(i!=j):
                    m=max(m,int(s[i])*int(s[j]))
        return m

        
