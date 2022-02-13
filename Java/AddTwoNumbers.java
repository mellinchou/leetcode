package Java;
// Problem Description: there are 2 linked lists that represents two numbers with digits stored in reversed order. add the two numbers together and return a linked list with the result, one digit in one node, in reverse order

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode result = new ListNode(0);
        ListNode head = result; //this is used to store the begining of the linked list
        
        int carry = 0; // use carry to store the carry digit
        while (l1 != null || l2 != null){
            int x = (l1!=null) ? l1.val : 0; //if the node is null, set x to 0
            int y = (l2!=null) ? l2.val : 0;
            int sum = x+y+carry;
            carry = sum/10; // carry is the amount divided by 10
            result.next = new ListNode(sum % 10); // the digit of the number is the remaining number after dividing by 10
            result=result.next;
            if(l1!=null) l1= l1.next;
            if(l2!=null) l2=l2.next;
        }
        if (carry>0){
            result.next=new ListNode(carry); //if the last digit has a carry digit, create one more node with value being the carry digit
        }
        return head.next; // since the first node is 0, return the head.next node
    }
}
