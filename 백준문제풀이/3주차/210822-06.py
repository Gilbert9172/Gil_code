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

# count += 1 을 써야한다.
# for문? while문?
# 마지막엔 합을 구해야함.

N = int(input())

for i in range(N):
    n = input()
    data = n.split('X')

    num = [i for i in data if len(i)>0]

    lst = []
    for i in range(len(num)):
        for j in range(len(num[i])):
            lst.append(j+1)
            sum_list = sum(lst)
        print(sum_list)