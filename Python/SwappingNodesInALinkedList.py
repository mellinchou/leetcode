from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=k_end=head
        index=1
        
        while dummy!=None:
            if index==k:
                k_begin=dummy
            elif index>k:
                k_end=k_end.next
            index+=1
            dummy=dummy.next
        k_begin.val, k_end.val= k_end.val, k_begin.val
        return head