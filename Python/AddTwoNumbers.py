from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        res = curr = ListNode(0)
        while l1!=None or l2!=None:
            if l1==None: l1=ListNode(0)
            elif l2==None: l2=ListNode(0)
            curr.next=ListNode((l1.val+l2.val+carry)%10)
            carry=int((l1.val+l2.val+carry)/10)
            curr=curr.next
            l1=l1.next
            l2=l2.next
        if carry!=0: curr.next=ListNode(carry)
        return res.next