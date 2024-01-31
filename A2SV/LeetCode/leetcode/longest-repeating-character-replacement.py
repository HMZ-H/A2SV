class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        count = defaultdict(int)
        max_oc = 0
        ans = 0
        while right < len(s):
            count[s[right]] += 1
            max_oc = max(max_oc, count[s[right]])
            if right-left+1 - max_oc > k:
                count[s[left]] -= 1
                left += 1
            else:
                ans = max(ans, right-left + 1)

            # if len(count) > 1:
            #     while sum(sorted(count.values())[:-1]) > k:
            #         count[s[left]] -= 1
            #         if count[s[left]] == 0:
            #             count.pop(s[left])
                    
            #         left += 1
            # ans = max(ans, right-left + 1)
            right += 1
        
        return ans