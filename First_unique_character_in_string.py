class Solution(object):
    def firstUniqChar(self, s):
        f={}
        for i in s:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        t=False
        ind=0
        for i in range(len(s)):
            if f[s[i]]==1:
                ind=i
                t=True
                break
        if t:
            return ind
        else:
            return -1
