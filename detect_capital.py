class Solution(object):
    def detectCapitalUse(self, word):
        s=word.upper()
        r=word.lower()
        if word==s or word==r or (word[0]==word[0].upper() and word[1:len(word)]==word[1:len(word)].lower()):
            return True
        else:
            return False
        
