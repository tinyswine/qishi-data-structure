class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        cnt_dict = {}
        
        for num in nums:
            cnt_dict[num] = cnt_dict.get(num, 0) + 1
        
        cnt_list = []
        for key in cnt_dict.keys():
            cnt_list.append((cnt_dict[key], key))
            
        j = 0
        result_list = []
        for cnt, num in sorted(cnt_list, reverse=True):
            result_list.append(num)
            j += 1
            if j == k:
                return result_list