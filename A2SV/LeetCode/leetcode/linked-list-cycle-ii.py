# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        iscycle = False
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                iscycle = not iscycle
                break
        if not iscycle:
            return
        slow = head
        while fast.next:
            if fast == slow:
                return slow
            slow = slow.next
            fast = fast.next
        