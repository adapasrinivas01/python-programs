class Solution(object):
    def averageValue(self, nums):  
        s=0
        j=0
        for i in nums:
            if i%2==0 and i%3==0:
                s+=i
                j+=1
        if j==0:
            return 0
        else:
            return s//j
