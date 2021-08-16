"""
문제번호 : 10818

제목 : 1차원 배열 / 최소, 최대

알고리즘 분류 : 수학, 구현

문제
- N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
- 1 ≤ N ≤ 1,000,000
"""

# 내장 함수(min,max) 사용
import sys

N = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))

Max = max(a)
Min = min(a)

print(Min, Max)

# sort 사용
import sys

N = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))
a.sort()

Max = a[-1]
Min = a[0]

print(Min,Max)

