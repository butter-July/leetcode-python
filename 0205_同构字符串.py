class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s2t,t2s={},{}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if (s[i] in s2t and t[i] !=s2t[s[i]]) or (t[i] in t2s and s[i]!=t2s[t[i]]):
                return False
            s2t[s[i]]=t[i]
            t2s[t[i]]=s[i]
        return True
