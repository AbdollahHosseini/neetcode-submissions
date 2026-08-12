# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev = None
        curr = head

        count = 1
        while curr and curr.next:
            count += 1
            curr = curr.next

        curr = head

        if n == 1 and count == 1:
            return head.next


        reach = count - n

        while reach >= 1 and curr and curr.next:
            prev = curr
            curr = curr.next
            reach -= 1

        if prev:
            prev.next = curr.next
        else:
            head = curr.next

        curr.next = None

        return head

