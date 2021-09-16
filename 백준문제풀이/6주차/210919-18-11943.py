"""
문제번호 : 11943
단계 : 	Bronze4
제목 : 파일 옮기기
알고리즘 분류 : 구현
"""

A, B = map(int, input().split())
C, D = map(int, input().split())

print(min(A+D,B+C))