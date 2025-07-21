import sys
sys.stdin = open('input.txt','r')


text = input()
text = text.strip()
if(text==""):
    print(0)
else:
    text = list(text)
    cnt = 1
    for i in range(0,len(text)):
        if(i == 0 and text[i] == ' '):
            continue
        if(i == len(text)-1 and text[i] == ' '):
            break
        if(text[i] == ' '):
            cnt += 1

    print(cnt)