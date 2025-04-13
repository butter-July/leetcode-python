class Solution:
    def countSegments(self, s):
        count=0
        i=0
        for i in range(len(s)):
            if (i==0 and s[i]!=" ") or (s[i]!=" " and s[i-1]==" "):
                count+=1
        return count
