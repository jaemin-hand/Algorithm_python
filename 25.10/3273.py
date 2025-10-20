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

for i in range(N):
    pass

# for i in range(N):
#     for j in range(i+1,N):
#         if(array[i] + array[j]) == M:
#             count += 1


print(count)
