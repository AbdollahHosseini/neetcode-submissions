# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        power = 0

        nodes = None
        last = None

        carry = 0

        while l1 or l2:
            val = carry
            carry = 0

            if l1:
                val += l1.val * (10**power)

            if l2:
                val += l2.val * (10**power)

            if val >= 10:
                carry = val // 10
                val = val % 10

            l1 = l1.next
            l2 = l2.next

            node = ListNode(val)

            if not nodes:
                nodes = node
                last = node
            else:
                last.next = node
                last = node

        if carry > 0:
            node = ListNode(carry)
            last.next = node
            last = node


        return nodes
            

        

        
        