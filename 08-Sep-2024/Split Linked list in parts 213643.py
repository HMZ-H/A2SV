# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = []
        leng = 0
        temp = head
        while temp:
            temp = temp.next
            leng +=1
        size, extra = divmod(leng, k)
        curr = head
        for i in range(k):
            head = temp = ListNode(None)
            for i in range(size+(i<extra)):
                temp.next = temp = ListNode(curr.val)
                if curr:
                    curr = curr.next
            res.append(head.next)
            k -=1
    
        return res
    
        