"""
문제번호 : 2530
단계 : 	Bronze4
제목 : 인공지능 시계
알고리즘 분류 : 수학 / 사칙연산
"""

A,B,C = map(int,input().split())
K = int(input())

C += K%60
K = K//60
if C >= 60:
    C -= 60
    B += 1

B += K%60
K = K//60
if B >= 60:
    B -= 60
    A += 1

A += K%24
if A > 23:
    A -= 24

print(A,B,C)


