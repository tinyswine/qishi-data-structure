class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        result_list = []
        
        num_dict = {}
        for i in nums1:
            num_dict[i] = num_dict.get(i, 0) + 1
            
        for j in nums2:
            if num_dict.get(j, 0):
                result_list.append(j)
                num_dict[j] -= 1
                
        return result_list