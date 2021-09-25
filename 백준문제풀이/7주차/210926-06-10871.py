import sys

N,X = map(int,sys.stdin.readline().split())

a = map(int,sys.stdin.readline().split())

for i in a:
    if i < X:
        print(i)