# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        found = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow==fast:
                found = True
                break
        if not  found:
            return None
        
        cur = head
        while cur!=slow:
            cur = cur.next
            slow = slow.next
        return slow
        