class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        counte=0
        length=len(word)
        for i in word:
            if i == i.upper():
                counte+=1
        if counte==length or (counte==1 and word[0]==word[0].upper() ) or counte==0:
            return True
        else:
            return False
