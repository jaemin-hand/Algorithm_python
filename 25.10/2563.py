import sys
sys.stdin = open('input.txt','r')

# 가로 세로 100 인 도화지가 있음
# 세로 크기가 각각 10인 정사각형(넓이100) 가 도화지 위로 올라감
# 종이가 붙은 영역의 넓이를 출력한다.


# 첫째줄에는 종이의 개수
paper_ex = int(input())

# 두번째줄에는 한줄에 하나씩 색종이를 붙인 위치가 주어진다.
# 색종이를 붙인 위치는 두 개의 자연수로 주어지는데,
# 첫번째 자연수는 색종이의 왼쪽변과 도화지의 왼쪽 변 사이의 거리.
# 두번째 자연수는 색종이의 아래쪽변과 도화지의 아래쪽 변 사이의 거리.

array = [[0] * 100 for _ in range(100)]
for _ in range(paper_ex):
    a,b = map(int,input().split())
    for i in range(10):
        for j in range(10):
            array[b-1+i][a-1+j] = 1

result = 0
for i in range(100):
    for j in range(100):
        result += array[i][j]
print(result)