import sys
sys.stdin = open('input.txt','r')

N = int(input())
# 컴퓨터 갯수

M = int(input())
# 노드값 받는 횟수

node = [[] for _ in range(N + 1)]

# 양방향 노드 연결
for i in range(M):
    a,b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)

result = 0
# 결과를 위한 카운팅

visited = [0] * (N + 1)
# 방문흔적 0인덱스 고려하여 N + 1

def dfs(start):
    global result
    visited[start] = 1
    # 방문흔적 남기기 0 -> 1

    for next in node[start]:
        if visited[next] == 0:
            result += 1
            dfs(next)
    pass

dfs(1)

print(result)