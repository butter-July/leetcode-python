class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        same=""
        for j in range(len(strs[0])):                          
            current_char=strs[0][j]                 #从第一个字符串的最后一个元素开始for
            for i in range(1,len(strs)):
                if j>=len(strs[i]) or strs[i][j]!=current_char:             #长度短或者是不相等就直接return代表着循环结束,same值不发生变化,如果不成立那么same就发生变化
                     return same
            
            same+=current_char
        return same
        
