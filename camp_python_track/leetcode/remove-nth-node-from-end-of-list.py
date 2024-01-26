class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_start = ListNode(0)
        new_start.next = head
        fast = new_start
        slow = new_start
        for _ in range(n):
            fast = fast.next
        #the fast head is n steps ahead of the slow head and will go len-n step till the end is found.that is the trick
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return new_start.next
        #time complexity O(N)
        #space complexity O(1)