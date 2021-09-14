"""
문제번호 : 10162
단계 : 	Bronze4
제목 : 전자레인지
알고리즘 분류 : 수학 . 구현 / 그리디 알고리즘
"""

# A 5분(300초)
# B 1분(60초)
# C 10초

T = int(input())

A = 0
B = 0
C = 0

while True:
    if T >= 300:
        T -= 300
        A += 1
    elif 60<= T < 300:
        T -= 60
        B += 1
    elif 10<= T < 60:
        T -= 10
        C += 1    
    elif T == 0:
        print(A,B,C)
        break
    else:
        print(-1)
        break