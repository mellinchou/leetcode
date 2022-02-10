# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        ptrA, ptrB = headA, headB
        
        while(ptrA!=ptrB):
            if(ptrA==None): ptrA=headB #append listB to the end of listA, for same length
            else: ptrA=ptrA.next
            
            if (ptrB==None): ptrB=headA
            else: ptrB=ptrB.next
        
        return ptrA