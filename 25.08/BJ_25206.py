import sys
sys.stdin = open('input.txt','r')

# output == (학점 * 등급)
# ex) 3.0 * A+

N = 20

DIC = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0
}

for _ in range(N):
    cnt = 0
    avg = 0
    summit = 0
    text = input().split()
    temp = []
    score = 0
    grade = ''
    for_result = 0
    # # text[len(text)-6:] == 3.0 A+
    if(text[-1] != 'P'):
        score = (float(text[1]))
        grade = text[2]
        cnt += 1
        for_result = score * DIC[grade]
    avg = for_result / cnt
    print(avg)