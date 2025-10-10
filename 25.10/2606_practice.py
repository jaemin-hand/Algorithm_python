import sys
sys.stdin = open('input.txt','r')

n = int(input()) # 컴퓨터 개수
m = int(input()) # 연결된 쌍의 수

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

count = 0 # 감염된 컴퓨터 수를 셀 변수

def dfs(start_node):
    global count # 함수 밖의 count 변수를 사용하겠다고 선언
    
    # 1. 현재 위치에 방문 도장 찍기
    visited[start_node] = True

    # 2. 현재 위치와 연결된 다음 장소들 확인
    for next_node in graph[start_node]:

        # 3. 만약 다음 장소가 아직 안 가본 곳이라면
        if not visited[next_node]:
            # 감염된 컴퓨터 수 1 증가
            count += 1

            # 그곳으로 다시 탐험 떠나기 (재귀 호출)
            dfs(next_node)

dfs(1)
print(count)