class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split()
        d=s[-1:]
    
        c=0
        for i in d[0]:
            c+=1

        return c
        
