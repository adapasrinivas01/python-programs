class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        s=sorted(nums1+nums2)
        l=len(s)
        if l%2!=0:
            return float(s[l/2])
        else:
            return (s[l//2-1]+s[l//2])/2.0
