import sys
sys.stdin = open("input.txt","r")

while(1):
    try:
        A = input()
    except EOFError:
        break
    print(A)
    