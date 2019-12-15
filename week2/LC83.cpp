/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        
        ListNode* x = head;
        if (head==NULL) return head;
        while (x->next!=NULL){
            if (x->next->val==x->val){
                x->next = x->next->next; 
            }
            else{
                x = x->next;
            }
        }
        return head;
    }
};