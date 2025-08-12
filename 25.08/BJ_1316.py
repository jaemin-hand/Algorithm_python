import sys
sys.stdin = open("input.txt",'r')



N = int(input())
result = 0
for _ in range(N):
    switch = 0
    stack = []
    text = input() # String 입력
    for i in range(len(text)): # a # ac # aca
        stack.append(text[i])
        if(i > 0):
            if(text[i] != text[i-1]):
                for ii in range(len(stack)-1):
                    if(text[i] == text[ii]):
                        switch = 1
                        break
        if(switch == 1):
            break
        if(i == len(text)-1):
            result += 1
    
print(result)