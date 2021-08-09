# 11021번 : A+B
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.(0 < A, B < 10)

import sys

N = int(sys.stdin.readline())

for i in range(N):
    A,B = map(int, sys.stdin.readline().split())
    Plus = A + B 
    i = i+1
    print(f'Case #{i}: {Plus}')
    
