"""
문제번호 : 10797
단계 : 	Bronze4
제목 : 10부제
알고리즘 분류 : 구현
"""

N = str(input())
data = map(str,input().split())

cnt = 0 
for i in data:
    if i.startswith(N) or i.endswith(N):
        cnt += 1
print(cnt)
