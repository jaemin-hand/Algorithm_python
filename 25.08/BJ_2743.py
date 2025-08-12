import sys
sys.stdin = open("input.txt",'r')

tc = int(input())
for i in range(tc):
    text = list(input())
    cnt = 0
    for _ in text:
        cnt += 1

    for _ in range(0,len(text)):
        if(cnt == 1 ):
            print(text[_],end='')
            print(text[_])
            break
        if(_ == 0):
            print(text[_],end='')
        if(_ == len(text)-1):
            print(text[_])