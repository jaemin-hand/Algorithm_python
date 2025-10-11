import sys
sys.stdin = open('input.txt','r')

cpu = int(input())
# 7

line = int(input())
# 6

node = [[] for _ in range(cpu + 1)]
# [ [] [] [] [] [] [] [] [] ]

for _ in range(line):
    a, b = map(int,input().split())
    # 1 , 2

    node[a].append(b)
    # node[1].append(2)
    # [ [] [1] [] [] [] [] [] [] ]

    node[b].append(a)
    # node[2].append(1)
    # [ [] [2] [1] [] [] [] [] [] ]

visited = [0] * (cpu + 1)

count = 0

def dfs(start):
    global count
    
    visited[start] = 1

    for i in node[start]:
        if visited[i] == 0:
            count += 1
            dfs(i)
    
dfs(1)

print(count)