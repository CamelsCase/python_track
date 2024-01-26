# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        store = []
        dummy.next = head
        for i in range(left):
            dummy = dummy.next
        ref = dummy
        for i in range(right-left+1):
            store.append(dummy.val)
            dummy = dummy.next
        for i in store[::-1]:
            ref.val = i
            ref = ref.next
        return head
        #time complexity O(2N)----> O(N)
        #space complexity O(N)