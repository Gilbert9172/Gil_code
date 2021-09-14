"""
문제번호 : 2752
단계 : 	Bronze4
제목 : 세수 정렬
알고리즘 분류 : 정렬
"""

N = list(set(map(int,input().split())))

N.sort()
for i in N:
    print(i,end=" ")