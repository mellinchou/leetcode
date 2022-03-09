from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None: return None
        res = curr = ListNode(0)
        while head!=None and head.next!=None:
            if head.val == head.next.val:
                while head.next!=None and head.val == head.next.val:
                    head.next=head.next.next
                head=head.next
            else:
                curr.next=ListNode(head.val)
                curr=curr.next
                head=head.next
        curr.next=head
        return res.next