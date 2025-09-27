class Solution(object):
    def reverseWords(self, s):
        s.replace("  "," ")   
        s=s.split()[::-1]
        return ' '.join(s)
