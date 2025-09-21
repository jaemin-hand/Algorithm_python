import sys
sys.stdin = open("input.txt",'r')

array = [[0] * 9 for _ in range(9)]

for i in range(9):
    array[i] = list(map(int,input().split()))

a = 0
b = 0

temp_max = 0
for i in range(9):
    for ii in range(9):
        if(temp_max < array[i][ii]):
            temp_max = array[i][ii]
            a = i
            b = ii

print(temp_max)
print(a+1,b+1)