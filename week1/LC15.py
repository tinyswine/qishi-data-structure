class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result_dict = {}
        for i in range(2, len(nums)):
            t = self.twosum(nums[:i], -nums[i])
            if t:
                for j in t:
                    tmp = j + [nums[i]]
                    tmp.sort()
                    result_dict[tuple(tmp)] = 1
        return [list(i) for i in result_dict.keys()]
        
        
    def twosum(self, nums, n):
        num_dict = {}
        result_list = []
        for i in nums:
            if not num_dict.get(n - i, 0):
                num_dict[i] = 1 
            else:
                result_list.append((i, n - i))
        t = list(set(result_list))
        return [list(i) for i in t]