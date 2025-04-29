class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1=0
        sum2=0
        n=len(nums) + 1
        for i in nums:
            sum1 += i
        for j in range(0,n):
            sum2 += j
        result = sum2-sum1
        return result
