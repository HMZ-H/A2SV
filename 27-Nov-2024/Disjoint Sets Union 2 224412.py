# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

from collections import defaultdict

n, m = map(int, input().split())
parent = {i : i for i in range(1, n + 1)}
rank = {i : 1 for i in range(1, n + 1)}
sets = {i : [i, i] for i in range(1, n + 1)}

def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x,y):
    parentX = find(x)
    parentY = find(y) 
    if parentY != parentX:
        if rank[parentX] < rank[parentY]:
            parent[parentX] = parentY
            rank[parentY] += rank[parentX]
            sets[parentY][0] = min(sets[parentY][0], sets[parentX][0])
            sets[parentY][1] = max(sets[parentX][1], sets[parentY][1])
        else:
            parent[parentY] = parentX
            rank[parentX] += rank[parentY]
            sets[parentX][0] = min(sets[parentX][0], sets[parentY][0])
            sets[parentX][1] = max(sets[parentY][1], sets[parentX][1])
   
for i in range(m):
    cmd, *u = input().split()
    if cmd == "union":
        union(int(u[0]), int(u[1]))
    else:
        x = find(int(u[0]))
        print(sets[x][0], sets[x][1], rank[x])

