import sys
sys.stdin = open('input.txt','r')

insert = input().strip()

result = 1

for i in range(len(insert)//2):
    if insert[i] != insert[-(i+1)]:
        result = 0
        break

print(result)