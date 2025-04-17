class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        low, high = 0, x
        if x==0:
            return 0
        if x==1:
            return 1
        while (low <= high):
            mid = (low + high) // 2
            if mid> x//mid:
                high = mid - 1
            else:
                low = mid + 1
        return int(high)
