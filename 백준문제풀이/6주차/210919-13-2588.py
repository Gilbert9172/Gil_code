"""
문제번호 : 2530
단계 : 	Bronze4
제목 : 곱셈
알고리즘 분류 : 수학 / 사칙연산
"""

a = input()
b = input()

c = int(a)*int(b[2])
d = int(a)*int(b[1])
e = int(a)*int(b[0])
f = c+d*10+e*100

print(c,d,e,f,sep="\n")