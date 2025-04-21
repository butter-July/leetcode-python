class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_sum(n):
            total=0
            while n>0:
                n,digit=divmod(n,10)
                total+=digit**2
            return total
        seen=set()
        while n !=1 and n not in seen:
            seen.add(n)
            n=get_sum(n)
        return n==1
