# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        a = ListNode(-102)
        prev = head
        a.next = prev
        cur = head
        while cur:
            while cur  and cur.val==prev.val:
                    cur = cur.next
            prev.next = cur
            prev = cur
        return a.next