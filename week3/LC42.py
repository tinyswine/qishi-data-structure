class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_list = []
        right_list = []
        for i in range(len(height)):
            if left_list:
                left_list.append(max(left_list[-1], height[i]))
            else:
                left_list.append(height[i])
                
                
        for i in range(len(height)):
            if right_list:
                right_list.append(max(right_list[-1], height[len(height) - i - 1]))
            else:
                right_list.append(height[len(height) - i - 1])
                
                
        area = 0
        for i in range(len(height)):
            area += min(left_list[i], right_list[len(height) - i - 1]) - height[i]
        return area