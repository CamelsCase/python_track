# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nw = ListNode(-102)
        cur1 = list1
        cur2 = list2
        head = nw
        while cur1 and cur2:
            if cur1 and cur2:
                if cur1.val<=cur2.val:
                    nw.next = cur1
                    nw = nw.next
                    cur1 = cur1.next
                else:
                    nw.next = cur2
                    nw = nw.next
                    cur2 = cur2.next 
        if cur1:
            nw.next = cur1
        elif cur2:
            nw.next = cur2
        return head.next