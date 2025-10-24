import sys
sys.stdin = open('input.txt','r')

N , B = input().split()

def change(value):
    if value >= '0' and value <= '9':
        return int(value)
    else:
        return ord(value) - 55
