# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # lis = []
        # curr = head
        # while curr:
        #     lis.append(curr.val)
        #     curr = curr.next
        
        # return lis == lis[::-1]
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            curr = slow.next
            slow.next = prev
            prev = slow
            slow = curr
        l, r = head, prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True
        