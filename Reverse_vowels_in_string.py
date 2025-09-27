class Solution(object):
    def reverseVowels(self,s):
        v="AEIOUaeiou"
        r=[i for i in s if i in v]
        r=r[::-1]
        s=list(s)
        j=0
        for i in range(0,len(s)):
            if s[i] in v:
                s[i]=r[j]
                j+=1
            
        return ''. join(s)
                
            
