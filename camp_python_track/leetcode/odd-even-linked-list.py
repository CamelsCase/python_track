# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        even = head
        prev= None
        even_dummy = ListNode(0)
        even_dummy.next = even
        odd = head.next
        odd_dummy = ListNode(1)
        odd_dummy.next = odd
        while even:
            try:
                even.next =even.next.next
                prev = even#this prev make the code work when the number of elements is even
                even = even.next
                odd.next  = odd.next.next
                odd = odd.next
            except:
                try:
                    even.next =even.next.next
                    even = even.next
                except:
                    break
                break
        even_dummy= even_dummy.next
        if even:
            even.next=odd_dummy.next
        else:
            prev.next = odd_dummy.next
        return head
        #time complexity O(N)
        #space complextity O(1)