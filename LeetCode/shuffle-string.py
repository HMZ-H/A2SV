class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        sorted_items = sorted(zip(s, indices), key=lambda item: item[1])
        sorted_keys = [item[0] for item in sorted_items]
        return ''.join(sorted_keys)
