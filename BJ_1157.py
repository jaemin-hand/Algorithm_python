import sys
sys.stdin = open('input.txt','r')

text = input().strip().upper()

# ord('A') 는 String 을 아스키숫자로 변환하는.
# 반대로 숫자를 문자로 변환하는 chr(65)

# [0] 배열 26개 생성
array = [0] * 26 

# 아스키숫자로 변환 후 배열에 카운팅
for i in range(0,len(text)):
    array[ord(text[i]) - 65] += 1

result = '?' 
counter = 0
same = 0
maxIdx = 0

for i in range(0,26):
    if(array[maxIdx] < array[i]):
        maxIdx = i

for i in range(0,26):
    if(array[i] == max(array)):
        counter += 1

for i in range(0,26):
    result = chr(maxIdx + 65)

if(counter > 1):
    result = '?'

print(result)