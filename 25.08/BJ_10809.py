import sys
sys.stdin = open('input.txt','r')

S = list(input())


Alpa = list('abcdefghijklmnopqrstuvwxyz')

for i in Alpa:
    for ii in range(0,len(S)):
        if(i == S[ii]):
            print(ii,end=' ')
            break
        if(ii == len(S)-1):
            print(-1,end=' ')