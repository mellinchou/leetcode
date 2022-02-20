# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = curr = ListNode(0)
        isMerge=False
        tempSum=0
        while head:
            if head.val==0 and isMerge==False:
                isMerge=True
                
            elif head.val==0 and isMerge==True:
                #add up sum and add to node
                curr.next=ListNode(tempSum)
                tempSum=0
                curr=curr.next
            else:
                tempSum+=head.val
            
            head=head.next
        return res.next