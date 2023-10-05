# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_list, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = new_list
            new_list = curr
            curr = nxt
            
        return new_list
