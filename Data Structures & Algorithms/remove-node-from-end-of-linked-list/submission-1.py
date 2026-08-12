# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev = None
        curr = head

        if n == 1:
            return head.next

        while n >= 1 and curr and curr.next:
            prev = curr
            curr = curr.next
            n -= 1

        prev.next = curr.next
        curr.next = None
        curr = curr.next

        return head

