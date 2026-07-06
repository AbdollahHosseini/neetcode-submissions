# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head:
            if not head.next:
                return False
        else: return False

        p1 = head
        p2 = head.next

        while p1 != p2 and p1 and p2:
            try:
                p1 = p1.next
                p2 = p2.next.next
            except:
                return False

        if p1 == p2:
            return True
        else: return False

        