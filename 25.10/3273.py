import sys
sys.stdin = open('input.txt','r')

N = int(input())
# 수열의 수

array = list(map(int,input().split()))

array.sort()


M = int(input())

count = 0

start = 0
end = N-1

while(end - start != 0):
    if(array[start] + array[end] == M):
        count += 1
        start += 1
    elif(array[start] + array[end] < M):
        start+=1
    else:
        end-=1



print(count)
