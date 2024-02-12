# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        pa = headA
        pb = headB
        la = 0
        lb = 0
        while a or b:
            if a:
                a = a.next
                la+=1
            if b:
                b = b.next
                lb+=1

        while pa and pb:
            while lb-la>0:
                pb = pb.next
                lb-=1
            while la-lb>0:
                pa = pa.next
                la-=1
            if pa==pb:
                return pa
            pa = pa.next
            pb = pb.next
            
        return None
                
            