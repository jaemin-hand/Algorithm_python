import sys
sys.stdin = open('input.txt','r')

cpu = int(input())

connect = int(input())

node = [[] for _ in range(cpu + 1)]

for _ in range(connect):
    a,b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)

count = 0

visited = [0] * (cpu + 1)

def dfs(start):
    global count
    visited[start] = 1
    for next in node[start]:
        if visited[next] == 0:
            count += 1
            dfs(next)

dfs(1)
print(count)