class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
       
        n=int("".join(map(str, digits))) 
        n=n+1
        s=[int(i) for i in str(n)]
        return s
        
