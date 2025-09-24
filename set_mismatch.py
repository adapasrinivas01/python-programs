class Solution(object):
    def findErrorNums(self, nums):
        f={} 
        for i in nums:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        n=set(nums)
        r=[i for i in n if f[i]>1]
        m=[j for j in range(1,len(nums)+1) if j not in nums]
        return r+m
                
