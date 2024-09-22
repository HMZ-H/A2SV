# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
       

        colors = [-1] * len(graph)

        def dfs(node, graph):
            temp = True
            for nd in  graph[node]:
                if colors[nd] == -1:
                    colors[nd] = 0 
                    if colors[node] == 1:
                        colors[nd] = 0 
                    else:
                        colors[nd] =  1
                    temp = temp and dfs(nd,graph)
                else:
                    temp = temp and colors[nd] != colors[node]

            return temp

        ans = True
        for node in range(len(graph)):
            if colors[node] == -1:
                colors[node] = 0
                ans = ans and dfs(node,graph)
        return ans
        