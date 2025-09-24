class Solution(object):
    def findComplement(self, num):
        b=bin(num)[2:]
        c=""
        for i in b:
            if i=='1':
                c+='0'
            else:
                c+='1'
        return int(c,2)
