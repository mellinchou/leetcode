from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = curr = ListNode(0)
        curr.next = head
        
        for i in range (0,n):
            head = head.next
        
        while head!=None:
            head=head.next
            curr=curr.next
        curr.next=curr.next.next
        
        return res.next