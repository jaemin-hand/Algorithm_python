import sys
sys.stdin = open('input.txt','r')

# https://www.acmicpc.net/problem/1193

X = int(input())

# 1 1/1
# 2 1/2
# 3 2/1
# 4 3/1
# 5 2/2
# 6 1/3
# 7 1/4
# 8 2/3
# 9 3/2
# 14 2/4

line = 1

while X > line:
    X = X - line # X에서 층의 분수 개수를 빼고
    line = line + 1

if line % 2 == 0:
    numerator = X
    denominator = line - X + 1
else:
    numerator = line - X + 1
    denominator = X

print(f"{numerator}/{denominator}")