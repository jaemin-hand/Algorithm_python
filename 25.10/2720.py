import sys
sys.stdin = open('input.txt','r')

T = int(input())
# 테스트케이스

# quarter = 25
# dime = 10
# nickel = 5
# penny = 1

array = []
for tc in range(T):
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0
    C = int(input())
    
    while(C != 0):
        if(C // 25):
            quarter += 1
            C -= 25
        elif(C // 10):
            dime += 1
            C -= 10
        elif(C // 5):
            nickel += 1
            C -= 5
        else:
            penny += 1
            C -= 1
    print(quarter, dime, nickel, penny)