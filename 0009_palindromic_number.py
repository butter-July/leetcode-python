思路
将数字转化为字符串使用str,然后开始判定是否是回文数,负数直接returnFalse,接下来看其他情况使用切片[::-1]以-1为步长进行切片实现字符串的反转,然后比较字符串是否相等
解题过程
直接调用所需知识即可
复杂度
时间复杂度: 
O(1)
﻿﻿
作者：buter-Jyly
链接：https://leetcode.cn/problems/palindrome-number/solutions/3625891/leetcodejian-dan-ti-by-goofy-archimedesf-g8dt/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        if str(x)==str(x)[::-1]:
            return True
        else:
            return False
