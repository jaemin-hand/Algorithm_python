import sys
sys.stdin = open("input.txt",'r')

text = input()

cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in cro:
    text = text.replace(i,' ')

print(len(text))