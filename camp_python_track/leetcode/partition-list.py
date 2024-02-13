# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lesser = ListNode()
        headl = lesser
        greater = ListNode()
        headg = greater
        cur = head
        while cur:
            if cur.val<x:
                lesser.next = cur
                cur = cur.next
                lesser = lesser.next
                lesser.next = None
            else:
                greater.next = cur
                cur = cur.next
                greater = greater.next
                greater.next = None
        lesser.next = headg.next
        return headl.next
                