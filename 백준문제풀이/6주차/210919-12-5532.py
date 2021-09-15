"""
문제번호 : 2530
단계 : 	Bronze4
제목 : 방학 숙제
알고리즘 분류 : 수학 / 사칙연산
"""

Days = int(input())
Math = int(input())
Kor = int(input())
M_p = int(input())
K_p = int(input())

lst = []

m = Math//M_p
if 0 < Math%M_p <= M_p:
    m = m+1
    lst.append(m)
else:
    lst.append(m)

k = Kor//K_p
if 0 < Kor%K_p <= K_p:
    k = k+1
    lst.append(k)
else:
    lst.append(k)

print(Days-max(lst))