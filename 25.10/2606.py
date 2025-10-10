import sys
sys.stdin = open('input.txt','r')


def dfs(start_node):
    global count
    visited[start_node] = True
    for next_node in graph[start_node]:
        if not visited[next_node]:
            count += 1
            dfs(next_node)
    pass

cpu = int(input())

N = int(input())
count = 0
graph = [[] for _ in range(cpu + 1)]

for _ in range(N):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

dfs(1)
print(count)