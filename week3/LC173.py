# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.val_list = self.inorderTraversal()
        self.cnt = 0
            
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.val_list.append(node.val)
            self.inorder(node.right)
    
    def inorderTraversal(self):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.val_list = []
        self.inorder(self.root)
        return self.val_list

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        self.cnt += 1
        return self.val_list[self.cnt - 1]
            

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.cnt == len(self.val_list):
            return False
        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()