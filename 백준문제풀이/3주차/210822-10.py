"""
문제번호 : 1065 

단계 : 함수

제목 : 한수

알고리즘 분류 : 수학 / 구현

문제 :  어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
        등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고,
        N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

입력 : 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
"""

# x = 110
# 1 <= N <= 110
# 110 보다 작은 수 중에서 한수는??

# 한수 
# 123 -> 1,2,3 공차가 +1인 한수
# 1357 -> 1,3,5,7 공차가 +2인 한수

# a = 1357

# b = list(map(int,str(a)))

# print(b)

# lst = []
# for i in range(len(b)-1):
#     minus = b[i]-b[i+1]
#     lst.append(minus)

# print(lst)
# if len(set(lst))==1:
#     print(a)


import sys
N = int(sys.stdin.readline())

gil = []
for i in range(1,N+1):

    if i < 10:
        gil.append(i)
        
    x = list(map(int,str(i)))

    lst = []
    for j in range(len(x)-1):
        minus = x[j]-x[j+1]
        lst.append(minus)
        
    if len(set(lst))==1:
        gil.append(i)

print(len(gil))