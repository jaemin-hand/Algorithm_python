import sys
sys.stdin = open('input.txt','r')

N = int(input())
M = int(input())

node = [[] for _ in range(N + 1)]
# 연결된 횟수 보다 1더 받아서 0인덱스 신경쓰기

for _ in range(M):
    a,b = map(int,input().split())
    # a, b 에 우선 노드값 받기

    node[a].append(b)
    node[b].append(a)
    # [a,b] a번 노드에 b연결되어있다 흔적남기기
    #       b번 노드에 a연결되어있다 흔적남기기

visited = [0] * (N+1)
# 방문흔적 0, 1로 표시

counter = 0

def dfs(start_node):
    global counter
    # counter 가져와서 쓰기

    visited[start_node] = 1
    
    for next_node in node[start_node]:
        # start_node 가 1로 들어오니, node[1]
        if not visited[next_node]:
            counter += 1
            dfs(next_node)

dfs(1)
print(counter)