"""
문제번호 : 10101
단계 : 	Bronze4
제목 : 삼각형 외우기
알고리즘 분류 : 구현 기하학
"""

# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error

A = int(input())
B = int(input())
C = int(input())

if A==B==C:
    print('Equilateral')
elif A+B+C == 180 and (A==B or A==C or B==C):
    print('Isosceles')
elif A+B+C == 180 and A!=B!=C:
    print('Scalene')
elif A+B+C != 180:
    print('Error')