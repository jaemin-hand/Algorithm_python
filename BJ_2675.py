import sys
sys.stdin = open('input.txt','r')

tc = int(input())

for _ in range(tc):
    R, S = input().split()
    R = int(R)
    S = list(S)
    for i in S:
        print(i * R,end='')
    print()