"""
문제번호 : 10162
단계 : 	Bronze4
제목 : 주사위 세개
알고리즘 분류 : 수학 / 사칙연산
"""

N = list(map(int,input().split()))

lst = []
for i in N:
    cnt = N.count(i)

    if cnt == 3:
        k=10000+(i*1000)
        lst.append(k)

    elif cnt == 2:
        k=1000+(i*100)
        lst.append(k)
        
    elif cnt == 1:
        k=max(N)*100
        lst.append(k)

print(max(lst))