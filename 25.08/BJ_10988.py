import sys
sys.stdin = open('input.txt','r')

insert = list(input())

result = 0

if(len(insert) % 2 == 0): # even
    for i in range(0,len(insert)//2):
        if(insert[len(insert)//2 - (i+1)] == insert[len(insert)//2 + i]):
            result =1
        else:
            result = 0
            break
else: # odd
    for i in range(0,len(insert)//2):
        if(insert[len(insert)//2 - (i+1)] == insert[len(insert)//2 + (i+1)]):
            result = 1
        else:
            result = 0
            break
if(len(insert) == 1):
    result = 1
print(result)