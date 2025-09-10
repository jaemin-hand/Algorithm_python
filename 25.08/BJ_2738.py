import sys
sys.stdin = open('input.txt','r')

N , M = map(int,input().split())

array1 = [[0] * M for _ in range(N)]

array2 = [[0] * M for _ in range(N)]

for i in range(N):
    array1[i] = list(map(int, input().split()))

for i in range(N):
    array2[i] = list(map(int, input().split()))

result_array = [[0] * M for _ in range(N)]

for i in range(N):
    for ii in range(M):
        result_array[i][ii] = array1[i][ii] + array2[i][ii]

for i in range(N):
    for ii in range(M):
        print(result_array[i][ii],end=' ')
    print()