import sys
sys.stdin = open("input.txt","r")

N, M = map(int,input().split())
array = list(range(1, N+1))
for _ in range(M):
    i , j = map(int,input().split())
    array[i-1:j] = reversed(array[i-1:j])
print(*array)