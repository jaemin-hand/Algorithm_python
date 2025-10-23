import sys
sys.stdin = open('input.txt','r')

N,B = input().split()

B = int(B)
# 진법으로 바꿀 B

def change(value):
    if value <= '9' and value >= '0':
        return int(value)
    else:
        return ord(value)-55

N = list(N)
result = 0
for i in range(1,len(N)+1):
    temp = B ** (i-1)
    result += change(N[-i]) * temp

print(result)