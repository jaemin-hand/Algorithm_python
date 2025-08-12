import sys
sys.stdin = open('input.txt','r')

text = input()

cro = {1:'c=',
       2:'c-',
       3:'dz=',
       4:'d-',
       5:'lj',
       6:'nj',
       7:'s=',
       8:'z='}

for pattern in cro.values():
    text = text.replace(pattern," ")

print(len(text))