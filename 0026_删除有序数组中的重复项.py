class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #快慢指针的存在
        slow=0
        fast=1
        while fast<len(nums):
            if nums[slow]!=nums[fast]:
                slow+=1
                nums[slow]=nums[fast]
            else:
                fast+=1
        return slow+1
