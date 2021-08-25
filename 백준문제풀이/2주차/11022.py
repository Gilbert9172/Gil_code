import sys

N = int(sys.stdin.readline())

for i in range(N):
    A,B = map(int,sys.stdin.readline().split())
    a = A + B
    i = i+1
    print(f'Case #{i}: {A} + {B} = {a}')
