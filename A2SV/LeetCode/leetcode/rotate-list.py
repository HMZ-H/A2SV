class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        
        size = 1
        curr = head
        while curr.next:
            curr = curr.next
            size += 1
        
        curr.next = head
        
        k %= size
        rotate_size  = size - k -1
        new_tail = head
        
        for i in range(rotate_size):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None

        return new_head