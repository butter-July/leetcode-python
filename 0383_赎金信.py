class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine=list(magazine)
        for i in ransomNote:
            found=False
            for j in range(len(magazine)):
                if i ==magazine[j]:
                    found=True
                    magazine.pop(j)
                    break
            if not found:
                return False
        return True
