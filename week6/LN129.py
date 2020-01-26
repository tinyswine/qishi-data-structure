"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        
        capacity = len(hashTable) * 2
        hashTable_new = [None for i in range(capacity)]
        
        for i in range(len(hashTable)):
            node = hashTable[i]
            while node:
                mod = node.val % capacity
                node_new = ListNode(node.val)
                if hashTable_new[mod]:
                    cur = hashTable_new[mod]
                    while cur:
                        pre = cur
                        cur = cur.next
                    pre.next = node_new
                else:
                    hashTable_new[mod] = node_new
                node = node.next
        
        return hashTable_new