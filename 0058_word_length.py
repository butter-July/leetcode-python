#method 1
class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.rstrip()
        length=0
        i=len(s)-1             #i=len(s)-1而不是len(s)的原因是索引从0开始而不是1
        while i>=0 and s[i]!=' ':
            length+=1
            i-=1              #i-=1的目的是使得循环向前进
        return length

#2
class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.rstrip()
        length=0
        for i in range(len(s)):
          if s[i]!=' ':
            length+=1
          else:
            length=0
        return length
