# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        
        def issame(left, right):
            if (not left) and (not right):
                return True
            if (not left) or (not right):
                return False
            
            part1 = (left.val == right.val)
            part2 = issame(left.left, right.right) & issame(left.right, right.left)
            
            return part1 & part2
        
        return issame(root.left, root.right)
        