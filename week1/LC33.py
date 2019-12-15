class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not len(nums):
            return -1
        
        left = 0
        right = len(nums) - 1
        
        if nums[right] >= nums[right - 1] and nums[right] >= nums[0]:
                pivot = left
                
        elif nums[right] <= nums[right - 1] and nums[right] <= nums[0]:
                pivot = right
        
        else:
            while left < right:
                mid = int((left + right) / 2)
                if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                    pivot = (mid + 1) % len(nums)
                    break
                elif nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                    pivot = mid
                    break
                elif nums[mid] >= nums[0]:
                    left = mid
                elif nums[mid] <= nums[-1]:
                    right = mid
        
        left = 0
        right = len(nums) - 1
        
        for i in [left, right]:
            if nums[self.get_index(nums, i, pivot)] == target:
                return self.get_index(nums, i, pivot)
        
        while left < right:
            mid = (left + right) / 2
            
            if (mid == left) or (mid == right):
                return -1
            
            left_num = nums[self.get_index(nums, left, pivot)]
            right_num = nums[self.get_index(nums, right, pivot)]
            mid_num = nums[self.get_index(nums, mid, pivot)]
            
            if mid_num == target:
                return self.get_index(nums, mid, pivot)
            elif mid_num < target:
                left = mid
            else:
                right = mid
            
        return -1
            
    def get_index(self, nums, index, pivot):
        if index + pivot < len(nums):
            return index + pivot
        return index + pivot - len(nums)