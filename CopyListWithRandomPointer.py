from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        res = copy = Node(0)
        curr = head
        while curr!=None:
            curr.next=Node(curr.val, curr.next, curr.random)
            curr=curr.next.next
        while head!=None:
            copy.next=head.next
            copy, head = copy.next, head.next.next
            if copy.random!=None:
                copy.random=copy.random.next
        return res.next