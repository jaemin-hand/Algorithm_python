import sys
sys.stdin = open("input.txt","r")

N = int(input())
scores = list(map(int,input().split()))

M = max(scores)
News = [s / M * 100 for s in scores]

avg = sum(News) / N

print(avg)