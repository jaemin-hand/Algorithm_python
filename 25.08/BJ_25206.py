import sys
sys.stdin = open('input.txt','r')

# output == (학점 * 등급)
# ex) 3.0 * A+ / sums

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
for_result = 0
sums = 0
for _ in range(N):
    avg = 0
    text = input().split()
    score = 0
    grade = ''
    # # text[len(text)-6:] == 3.0 A+
    # ex) 3.0 * A+
    # 전공평점 == 3.0 * A+ / sums
    if(text[-1] != 'P'):
        score = (float(text[1]))
        grade = text[2]
        sums += score
        if(grade != 'F'):
            for_result += score * DIC[grade]
if(sums == 0):
    nums = 0.0
    print("{:.6f}".format(nums))
else:
    avg = for_result / sums
    print("{:.6f}".format(avg))