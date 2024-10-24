# Problem: Minimum Time Taken by Each Job to be Completed Given by a DAG - https://practice.geeksforgeeks.org/problems/minimum-time-taken-by-each-job-to-be-completed-given-by-a-directed-acyclic-graph/1

from typing import List

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        graph=[[] for _ in range(n)]
        ans=[1 for _ in range(n)]
        deg=[0 for _ in range(n)]
        for edge in edges:
            u,v=edge[0]-1,edge[1]-1
            deg[v]+=1
            graph[u].append(v)
        queue=[]
        for i in range(n):
            if deg[i]==0:
                queue.append(i)
        # vis={}
        while len(queue):
            node=queue.pop()
            for child in graph[node]:
                deg[child]-=1
                if deg[child]==0:
                    ans[child]+=ans[node]
                    queue.append(child)
        return ans