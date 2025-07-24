import sys
sys.stdin = open('input.txt','r')
A = 2 + 1
D = 3+ 1
G = 4+ 1
J = 5+ 1
M = 6+ 1
P= 7+ 1
T = 8+ 1
W = 9+ 1
Alpa = list(input())
result = 0
for i in Alpa:
    if i == 'A' or i == 'B' or i == 'C':
        result += A
    elif i == 'D' or i == 'E' or i == 'F':
        result += D 
    elif i == 'G' or i == 'H' or i == 'I':
        result += G
    elif i == 'J' or i == 'K' or i == 'L':
        result += J
    elif i == 'M' or i == 'N' or i == 'O':
        result += M
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        result += P
    elif i == 'T' or i == 'U' or i == 'V':
        result += T
    elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
        result += W
print(result)