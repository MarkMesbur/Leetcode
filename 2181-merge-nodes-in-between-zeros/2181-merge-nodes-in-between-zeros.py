# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mergenodes = temp = ListNode()
        head = head.next
        while head.next:
            if head.val == 0:
                mergenodes.next = ListNode()
                mergenodes = mergenodes.next
            else:
                mergenodes.val += head.val
            head = head.next
        return temp