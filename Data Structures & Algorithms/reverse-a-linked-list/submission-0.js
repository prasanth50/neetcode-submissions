/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {ListNode}
     */
    reverseList(ListNode) {
           let curr=ListNode
            let prev=null;
           while(curr != null){
            
            let nextTemp=curr.next
            curr.next=prev;
            prev=curr;
            curr=nextTemp

            

           }
           return prev
           }
    
}
