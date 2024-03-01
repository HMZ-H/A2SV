class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if k == len(cookies):
            return max(cookies)
        min_unfer = float('inf')
        distru = [0]*k

        def backt(index):
            nonlocal min_unfer
            # print(distru)
            if index >= len(cookies):
                min_unfer = min(min_unfer, max(distru))
                return
            for i in range(k):
                distru[i]+= (cookies[index])
                backt(index + 1)
                distru[i] -= cookies[index]
        backt(0)
        return min_unfer

        