"""
문제번호 : 8958

제목 : 1차원 배열 / OX퀴즈

알고리즘 분류 : 구현
"""
"""
문제:
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, 

X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지

연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
"""

# N = int(input())

# # X를 기준으로 문자열 분리.
# for i in range(N):
#     n = input()

#     # 'X'를 기준으로 분리.
#     data = n.split('X')

#     # 분리한 분자열 중에 길이가 0보다 큰 것만 리스트로 반환
#     # ex. ["OO","","O","OOO"] => ["OO","O","OOO"]
#     num = [i for i in data if len(i)>0]

#     gil = []
#     for i in range(len(num)):
#         lst = []
#         for j in range(len(num[i])):     # ex) "OO"의 length는 2 => j; 0~1 => j+1; 1~2 
#             lst.append(j+1)              # ex) lst = [[1,2],[1],[1,2,3]]
#             sum_list = sum(lst)
#         gil.append(sum_list)             # ex) gil = [3,1,6]
#     print(sum(gil))


# str(N) ; sclicing때 유용할 듯.
from itertools import chain

N = input()
a = list(chain.from_iterable([N]))
print(a)