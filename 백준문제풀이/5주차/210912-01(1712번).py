"""
문제번호 : 1712
단계 : 	기본 수학1
제목 : 손익분기점
알고리즘 분류 : 수학 / 사칙연산
"""

# Gil_code_1 (try,except)
A,B,C = map(int,input().split())

try:
    x = A / (C - B)
    if C-B<0:
        print(int(-1))
    elif C-B > 0:
        print(int(x+1))
except ZeroDivisionError:
    print(int(-1))

# Gil_code_2
A,B,C = map(int,input().split())
if C-B>0:
    x = A / (C - B)
    print(int(x)+1)
else:
    print(int(-1))