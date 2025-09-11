class Solution(object):
    def arraySign(self, nums):
        p=1
        for i in nums:
            p=p*i
        if p>0:
            return 1
        elif p<0:
            return -1
        else:
            return 0

