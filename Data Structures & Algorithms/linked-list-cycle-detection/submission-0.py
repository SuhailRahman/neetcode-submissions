# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f = head
        s = head
        while f and f.next:
            f = f.next.next
            s = s.next
            if f == s:
                return True
        return False
            