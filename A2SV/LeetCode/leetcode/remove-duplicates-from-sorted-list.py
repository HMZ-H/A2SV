# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output=curr = head
        # while curr:
        #     while curr.next and curr.val==curr.next.val:
        #         curr.next=curr.next.next
        #     curr=curr.next
        # return output
        while curr:
            if curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return output
        