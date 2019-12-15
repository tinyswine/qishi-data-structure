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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* a=head;
        while (true){
            if (head==NULL) return head;
            else if (head->val==val) head = head->next;
            else break;
        }
        a = head;
        while (true){
            if (a->next==NULL) break;
            if (a->next->val==val) a->next = a->next->next;
            else a = a->next;
        }
        return head;
    }
};