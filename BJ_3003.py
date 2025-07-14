import sys
sys.stdin = open('input.txt','r')

array = list(map(int,input().split()))

compare = [1, 1, 2, 2, 2, 8]

result = []

for _ in range(0,6):
    result.append(compare[_] - array[_])
print(*result)