"""
문제번호 : 1297
단계 : 	Bronze4
제목 : TV 크기
알고리즘 분류 : 수학/기하학/피타고라스 정리
"""

A,B,C = map(int,input().split())

K = (A**2 / ((B**2)+(C**2)))**0.5

H = int(B*K)
W = int(C*K)

print(H,W)