"""
실전문제 : 왕실나이트
난이도 : 1 
"""

# 나이트가 해당 포지션에서 이동할 수 있는 경우의 수
# a1에 있을 경우 두 가지 경우 밖에 없다.

# 좌표 평면상에 임의의 점이 주어졌을 때 나이트가 움직일 수 있는 경우의 수를 나타내는 코드

a = ['a','b','c','d','e','f','g','h']


x = 1
y = 1

# 왼 -> 오
R = x + 2
D = y + 1 
U = y - 1 

# 오 -> 왼
L = x - 2 
D = y + 1 
U = y - 1 