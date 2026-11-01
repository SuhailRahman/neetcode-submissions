# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        
        f = head
        s = head
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
        
        l2_not_reversed = s.next
        s.next = None

        prev = None
        cur = l2_not_reversed
        while cur:
            ahead = cur.next
            cur.next = prev
            prev = cur
            cur = ahead
        l2 = prev
        l1 = head
        while l1 and l2:
            l1_next = l1.next
            l1.next = l2
            l1 = l1_next
            l2_next = l2.next
            l2.next = l1
            l2 = l2_next
        
        return
