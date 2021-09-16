"""
문제번호 : 10707
단계 : 	Bronze4
제목 : 수도 요금
알고리즘 분류 : 수학/사칙연산
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

A = a*e

if e>c:
    B =((e-c)*d)+b
else:
    B = b

print(min(A,B))