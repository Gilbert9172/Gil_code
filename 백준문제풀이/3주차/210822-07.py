"""
문제번호 : 4344

제목 : 1차원 배열 / 평균은 넘겠지

알고리즘 분류 : 수학 / 사칙연산
"""
"""
문제
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,

이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
"""


import sys
C =int(input())

for i in range(C):
    data = list(map(int,sys.stdin.readline().split()))

    # 학생의 수
    n = data[0]

    # 학생들의 총 점수
    total_score = sum(data[1:])

    # 평균
    avg = total_score / n

    # 평균 보다 높은 점수들만 list에 append
    score = []
    for j in data[1:]:
        if j > avg:
            score.append(j)

    # 평균 보다 높은 점수의 갯수
    upper_score = len(score)

    per = (upper_score/n)*100
    print("{:.3f}%".format(per))


"""
list.pop(n)
리스트 내 n번째 요소 제거 하기
"""