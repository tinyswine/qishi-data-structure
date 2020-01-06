class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        if not nums:
            return []
        
        num_list = []
        
        for i in range(k):
            heapq.heappush(num_list, (-nums[i], i))
        
        result_list = [-num_list[0][0]]
        
        for i in range(k, len(nums)):
            heapq.heappush(num_list, (-nums[i], i))
            while num_list[0][1] < i - k + 1:
                heapq.heappop(num_list)
            result_list.append(-num_list[0][0])
            
        return result_list
        