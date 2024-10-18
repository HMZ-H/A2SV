# Problem: Helpful Maths - https://codeforces.com/problemset/problem/339/A

t = input().split("+")
t.sort()
res = "".join([i + "+" for i in t])
print(res[:len(res)-1])
