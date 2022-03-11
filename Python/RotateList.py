from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None: return None
        curr = head
        length=1
        
        while curr.next!=None: # find the tail and append to head
            curr=curr.next
            length+=1
        curr.next=head
        
        for i in range (length-(k%length)): # loop until the first rotated node
            curr=curr.next
        res=curr.next
        curr.next=None
        return res