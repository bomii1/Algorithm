import sys

T = int(input())

for i in range(T):
    sentence = sys.stdin.readline().rstrip().split(" ")
#print(sentence)
    for j in sentence:
        print(j[::-1], end=" ")
