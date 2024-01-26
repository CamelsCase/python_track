# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        out = ""
        while cur:
            out+=str(cur.val)
            cur = cur.next
        return out==out[::-1]