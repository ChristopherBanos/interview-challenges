class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pairDict = dict()
        print(nums)
        for i in range(0, len(nums)):
            pair = target - nums[i]
            if pair not in pairDict:
                pairDict[pair] = i
        print(pairDict)
        
        for i in range(0, len(nums)):
            val = nums[i]
            if val in pairDict and pairDict[val] != i:
                p2= pairDict[val]
                p1 = i
                if p1 < p2:
                    return [p1, p2]
                else:
                    return [p2, p1]
        
        return [0,0]