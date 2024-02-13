# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return
        s = f = head
        curr = head
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
            if s is f:
                return True
        return False
        
        