"""
문제번호 : 10039
단계 : 	Bronze4
제목 : 평균점수
알고리즘 분류 : 수학 / 사칙연산
"""
# 코드1
lst = []
for i in range(5):
    N = int(input())
    if N < 40:
        N = 40
        lst.append(N)
    else:
        lst.append(N)
avg = int(sum(lst)/len(lst))
print(avg)

# 코드2
sum = 0
for i in range(5):
    N = int(input())
    if N < 40:
        sum += 40
    else:
        sum += N
print(sum/5)