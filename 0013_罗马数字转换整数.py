class Solution(object):
    def romanToInt(self, s):
        roman_to_int={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        total=0
        n=len(s)
        for i in range(n):
            current=roman_to_int[s[i]]
            if i<n-1 and current<roman_to_int[s[i+1]]:
                total-=current
            else :
                total+=current
        return total
