# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur1 = head
        cur2 = head
        if not head:
            return None
        while True:
            if not cur1.next:
                return None
            if not (cur1.next.next and cur2.next):
                return None
            cur1 = cur1.next.next
            cur2 = cur2.next
            if cur1 == cur2:
                break
        cur1 = head
        while True:
            if cur1 == cur2:
                return cur1
            cur1 = cur1.next
            cur2 = cur2.next