class Solution(object):
    def countKeyChanges(self, s):
        s=s.lower()
        s=sum(1 for i in range(len(s)-1) if s[i]!=s[i+1]) 
        return s
