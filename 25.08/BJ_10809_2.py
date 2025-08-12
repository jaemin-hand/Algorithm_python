import sys
sys.stdin = open('input.txt','r')

S = input()

alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in alphabet:
    print(S.find(i), end = ' ')