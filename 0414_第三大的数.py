class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        newnum=[]
        for num in nums:
            if num not in newnum:
                newnum.append(num)
        if len(newnum)<3:
            max=newnum[0]
            for i in newnum[1:]:
                if i>max:
                    max=i
            return max
        
        for i in range(len(newnum)):
            num_bigger=i
            for j in range(i+1,len(newnum)):
                if  newnum[num_bigger]<newnum[j]:
                    num_bigger=j
            newnum[i],newnum[num_bigger]=newnum[num_bigger],newnum[i]
        return  newnum[2]
                    
