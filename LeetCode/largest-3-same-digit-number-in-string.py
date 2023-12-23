class Solution:
    def largestGoodInteger(self, num: str) -> str:
        candidate = ""
        start = 0
        for i in range(1, len(num)):
            current, prev = num[i], num[i-1]
            if current == prev:
                if i - start + 1 == 3:
                    if candidate == "":
                        candidate = current
                    else:
                        candidate = max(int(candidate), int(current))
            else:
                start = i 
        return str(candidate) * 3
        