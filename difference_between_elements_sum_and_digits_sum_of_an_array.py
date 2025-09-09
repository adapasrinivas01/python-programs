class Solution(object):
    def differenceOfSum(self, nums):
        s=sum(i for i in nums)
        c=0
        for i in nums:
            i=str(i)
            c+=sum(int(j) for j in i)
        return max(s,c)-min(s,c)
            
