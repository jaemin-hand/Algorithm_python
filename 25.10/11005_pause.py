import sys
sys.stdin = open('input.txt','r')

N , B = input().split()
# N는 B진수로 변환해야할 10진수

def change(value):
    if value >= '0' and value <= '9':
        return int(value)
    else:
        return ord(value) - 55

