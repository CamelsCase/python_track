# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 

        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        i = 0
        arr.sort()
        temp = head
        while temp:
            temp.val = arr[i]
            i += 1
            temp = temp.next

        return head
        




        