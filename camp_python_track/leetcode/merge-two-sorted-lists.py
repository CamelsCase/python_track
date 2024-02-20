# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def do_the_magic(self,hd,merged,head1,head2):
        if merged ==None:
            merged = ListNode()
        if hd==None:
            hd = merged
        if head1==None:
            merged.next = head2
            return hd.next
        elif head2==None:
            merged.next = head1
            return hd.next
        elif head1.val<head2.val:
            merged.next = head1
            head1 = head1.next
        elif head1.val>=head2.val:
            merged.next = head2
            head2 = head2.next
        merged = merged.next
        next_call = self.do_the_magic(hd,merged,head1,head2)
        return hd.next
        
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ls = self.do_the_magic(None,None,list1,list2)
        return ls
    