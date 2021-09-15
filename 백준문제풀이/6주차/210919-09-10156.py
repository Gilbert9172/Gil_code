"""
문제번호 : 10156
단계 : 	Bronze4
제목 : 과자
알고리즘 분류 : 수학 / 사칙연산
"""

K,N,M = map(int,input().split())

x = (K*N)-M

if x < 0:
    print(0)
else:
    print(x)
