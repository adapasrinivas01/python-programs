class Solution(object):
    def majorityElement(self, nums):
        f={}    
        l=[]
        for i in nums:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        n=set(nums)
        ind=0
        for i in n:
            if (len(nums)/3)<f[i]:
                l.append(i)
                
        return l
                
