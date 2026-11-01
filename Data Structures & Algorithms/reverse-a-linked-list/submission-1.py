# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
            
        newHead = head
        while newHead.next:
            newHead = newHead.next
        
        def reverseL(cur):
            if not cur:
                return None
            
            ahead = reverseL(cur.next)
            if ahead:
                cur.next = ahead.next
                ahead.next = cur
            return cur
        
        reverseL(head)

        return newHead