# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=, LiteralString0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        start = None

        h1 = list1
        h2 = list2

        while h1 and h2:
            if h1.val < h2.val:
                if not newHead:
                    newHead = h1
                    start = newHead
                else:
                    newHead.next = h1
                    newHead = newHead.next
            
                h1 = h1.next
                newHead.next = None

            else:
                if not newHead:
                    newHead = h2
                    start = newHead
                else:
                    newHead.next = h2
                    newHead = newHead.next

                h2 = h2.next
                newHead.next = None    



        while h1:
            if not newHead:
                newHead = h1
                start = newHead
            else:
                newHead.next = h1
                newHead = newHead.next
            
            h1 = h1.next
            newHead.next = None
            
        while h2:
            if not newHead:
                newHead = h2
                start = newHead
            else:
                newHead.next = h2
                newHead = newHead.next

            h2 = h2.next
            newHead.next = None    

        return start   


            
            