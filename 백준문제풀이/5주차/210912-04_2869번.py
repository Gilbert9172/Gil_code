"""
문제번호 : 2869
단계 : 	기본 수학1
제목 : 달팽이는 올라가고 싶다
알고리즘 분류 : 수학
"""
# 접근 
# 1. A(낮 이동 거리), B(미끄러진 거리), V(막대의 길이)
# 2. H = A-B : 하루동안 달팽이가 이동한 거리
# 3. V = H*day + A 

# H가 1인 경우 : day = V-A+H
# H가 1보다 큰 경우 : day != V-A / H

from math import ceil

A,B,V = map(int,input().split())

H = A-B

if H == 1:
    print(V-A+H)
else:
    print(ceil((V-A)/H)+1)

"""
Ceil 함수
무조건 반올림 해준다.

ceil(1.2) = 1
ceil(-1.2) = -1
"""