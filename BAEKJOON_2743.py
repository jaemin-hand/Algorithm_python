import sys
sys.stdin = open("input.txt",'r')

text = list(input())
cnt = 0
for _ in text:
    cnt += 1
print(cnt)