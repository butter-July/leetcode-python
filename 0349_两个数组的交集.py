class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums3=[]
        for num1 in nums1:
            for num2 in nums2:
                if num1==num2 and num1 not  in nums3:
                    nums3.append(num1)
        return nums3
