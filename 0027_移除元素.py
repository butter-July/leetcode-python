class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        p=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[p]=nums[i]
                p+=1
        return p 
