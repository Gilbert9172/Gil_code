"""
문제번호 : 5543
단계 : 	Bronze4
제목 : 상근날드
알고리즘 분류 : 수학 / 사칙연산
"""
lst = []
for i in range(5):
    N = int(input())
    lst.append(N)

buger_min = min(lst[0:3])
bev_min = min(lst[3:5])
Total_Fee = buger_min + bev_min - 50

print(Total_Fee)