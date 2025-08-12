import sys
sys.stdin = open('input.txt','r')

tc = int(input())

array = list(map(int,input()))

result = sum(array)

print(result)