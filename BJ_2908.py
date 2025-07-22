import sys
sys.stdin = open('input.txt','r')

A, B = input().split()
A = A[::-1]
B = B[::-1]
A = int(A)
B = int(B)

print(A if A > B else B)