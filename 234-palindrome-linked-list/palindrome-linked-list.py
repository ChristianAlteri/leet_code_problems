# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current = head  
        arr = []
        while current:
            arr.append(current.val)
            current = current.next 
        l, r = 0, len(arr) - 1
        while l <= r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True 
        
        # print(mid)
    
        