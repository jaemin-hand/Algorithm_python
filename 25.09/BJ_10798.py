import sys
sys.stdin = open('input.txt','r')

texts = []
for _ in range(5):
    text = input()
    texts.append(text)

max_len = 0

for _ in range(5):
    if(max_len < len(texts[_])):
        max_len = len(texts[_])

result = []

for i in range(max_len):
    for ii in range(5):
        if(len(texts[ii]) > i):
            result += texts[ii][i]

print(''.join(result))