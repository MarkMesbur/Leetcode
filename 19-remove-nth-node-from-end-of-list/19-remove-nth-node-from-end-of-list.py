# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        delay = dummy
        
        for _ in range(n+1):
            first = first.next
        
        while first:
            first = first.next
            delay = delay.next
        
        delay.next = delay.next.next
        return dummy.next
            
        