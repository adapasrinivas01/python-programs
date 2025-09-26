class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        f={}
        for i in nums:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        l=[]
        n=set(nums)
        for i in n:
            if f[i]>=2:
                l.append(i)
        return l
