# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        tmpHead = head
        while tmpHead:
            tmpHead = tmpHead.next
            length += 1
        
        if (length - n) == 0:
            cur = head.next
            head.next = None
            return cur

        prev = None
        cur = head

        for i in range(length - n):
            prev = cur
            cur = cur.next
        
        if prev:
            prev.next = cur.next
            cur.next = None

        return head