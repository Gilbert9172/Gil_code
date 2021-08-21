"""
문제번호 : 1065 

단계 : 함수

제목 : 한수

알고리즘 분류 : 수학 / 구현

문제 :  어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
        등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고,
        N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
"""

# 한수 
# 123 -> 1,2,3 공차가 +1인 한수
# 1357 -> 1,3,5,7 공차가 +2인 한수

# 코드 1 
import sys
N = int(sys.stdin.readline())

gil = []
for i in range(1,N+1):

    # 10만의 수는 모두 한수 
    if i < 10:
        gil.append(i)

    # str slicing
    x = list(map(int,str(i)))

    lst = []
    # j+1번째 값과 j번째 값의 차이 
    for j in range(len(x)-1):
        minus = x[j+1] - x[j]
        lst.append(minus)
    
    # minus가 모두 같다면 
    if len(set(lst))==1:
        gil.append(i)

print(len(gil))

# 코드 2 (itertools 사용)
from itertools import chain
import sys

N = N = int(sys.stdin.readline())

gil =[]
for i in range(1,N+1):

    # 10만의 수는 모두 한수 
    if i < 10:
        gil.append(i)

    # itertools 사용 -> ['1','2','3']과 같은 형태로 나옴
    x = list(map(int,chain.from_iterable([str(i)])))

    lst = []
    # j+1번째 값과 j번째 값의 차이 
    for j in range(len(x)-1):
        minus = x[j+1] - x[j]
        lst.append(minus)
    
    # minus가 모두 같다면 
    if len(set(lst))==1:
        gil.append(i)

print(len(gil))
