import sys
sys.stdin = open("input.txt","r")

N = int(input())
scores = list(map(int,input().split()))

M = max(scores)

temp = []

for i in scores:
    temp.append(i / M * 100)

total = sum(temp)
avg = total / N

print(avg)