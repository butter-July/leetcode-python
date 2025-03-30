class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos=0                #记录0的位置
        for i in range(len(nums)) :
            if nums[i]!=0:           #这里是如果不是0,就储存他们的值在最前面然后让pos++
                nums[pos]=nums[i]
                pos+=1
        for i in range(pos,len(nums)):
            nums[i]=0              #所有不是0的都放在了前面所以可以开始在后面+0,pos和len差几就是差了几个0
                

        
