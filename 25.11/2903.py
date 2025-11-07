import sys
sys.stdin = open('input.txt','r')

N = int(input())

ready = 2
temp = ready ** N

print(((2 ** N) + 1)*((2**N)+1))