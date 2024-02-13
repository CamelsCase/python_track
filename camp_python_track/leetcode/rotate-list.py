# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        leng = 1 if head else 0
        if leng!=0:
            cur = head
            while cur and cur.next:
                leng+=1
                cur = cur.next
            cur.next = head
            moves = k%leng
            while leng-moves-1>=0:
                cur = cur.next
                moves+=1 
            head = cur.next
            cur.next = None
        return head
        #TIME COMPLEXITY O(2*{LENGTH OF THE LINKED LIST}-K) = O(N)
        #SPACE COMPLEXITY O(1)

        