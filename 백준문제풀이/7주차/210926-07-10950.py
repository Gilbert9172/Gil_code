import sys

N = int(sys.stdin.readline())

for i in range(N):
    data = list(map(int,sys.stdin.readline().split()))
    a = sum(data)
    print(a)