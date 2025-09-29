class Solution(object):
    def maxFrequencyElements(self,nums):
            f={}
            for i in nums:
                if i in f:
                    f[i]+=1
                else:
                    f[i]=1
            m=max(f.values())
            nums=set(nums)
            s=sum(f[i] for i in nums if f[i]==m)
            return s
