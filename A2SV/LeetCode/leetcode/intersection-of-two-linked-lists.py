# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # h1 = headA
        # h2 = headB
        # res = None
        # dic = defaultdict(ListNode)
        # while h1:
        #     dic[h1] = h1.next
        #     h1 = h1.next
        # while h2:
        #     if h2 in dic and dic[h2] == h2.next:
        #         res = h2
        #         break
        #     h2 = h2.next
        # return res
        h1 = headA 
        h2 = headB
        n, m = 0,0
        while h1:
            n +=1
            h1 = h1.next
        while h2:
            m +=1
            h2 = h2.next
        h1, h2 = headA, headB
        while n !=m:
            if n >m:
                h1 = h1.next
                n-=1
            else:
                h2 = h2.next
                m-=1
        while h1 and h2:
            if h1 == h2:
                return h1
            else:
                h1 = h1.next
                h2 = h2.next
        return None
           