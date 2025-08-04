import sys
sys.stdin = open('input.txt','r')

N = int(input())

for i in range(1,N+1):
    star = 2 * i - 1
    void = N - i
    print(' ' * void + '*' * star)

for i in range(N-1, 0, -1):
    star = 2 * i - 1
    void = N - i
    print(' ' * void + '*' * star)