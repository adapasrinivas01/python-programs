class Solution(object):
    def reverseWords(self,s):
        s=s.split()
        rev=[w[::-1] for w in s]
        return ' '.join(rev)
        
