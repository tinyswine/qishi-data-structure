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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *l3,*l4;
        int add=0, count=0, sum, s1, s2;
        l3 = new ListNode(0);
        l4 = l3;
        while (1)
        {
            count++;
            
            if ((l1 == NULL) and (l2 == NULL))
            {
                if (add==1)
                {
                    l4->next = new ListNode(1);
                }
                break;
            } 
            
            if (l1 == NULL){
                s1 = 0;
            }
            else{
                s1 = l1->val;
                l1 = l1->next;
            }
            
            if (l2 == NULL){
                s2 = 0;
            } 
            else{
                s2 = l2->val;
                l2 = l2->next;
            }
            
            sum = s1+s2+add;
            add = 0;
            if (sum>=10)
            {
                add = 1;
                sum = sum-10;
            }
            if (count==1){
                l4->val = sum;
            }
            else
            {
                l4->next = new ListNode(sum);
                l4 = l4->next;
            }
        }
        return l3;
    }
};