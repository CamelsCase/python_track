# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast:
            try:
                fast = fast.next.next
                slow = slow.next
            except :
                if fast.next:
                    slow = slow.next
                break
        return slow
        