# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(float("inf"))
        newTail = newHead

        while list1 and list2:
            if list1.val < list2.val:
                newTail.next = list1
                list1 = list1.next
            else:
                newTail.next = list2
                list2 = list2.next
            newTail = newTail.next
        
        if list1:
            newTail.next = list1
        
        if list2:
            newTail.next = list2
        
        return newHead.next