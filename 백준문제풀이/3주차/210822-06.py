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

N = int(input())

# X를 기준으로 문자열 분리.
for i in range(N):
    n = input()
    data = n.split('X')

    # 분리한 분자열 중에 길이가 0보다 큰 것만 리스트로 반환
    # 예를 들면, ["OO","","O","OOO"] 이라면 
    # 반환 되는 리스트는 ["OO","O","OOO"]
    num = [i for i in data if len(i)>0]


    gil = []
    for i in range(len(num)):
        lst = []
        for j in range(len(num[i])):
            lst.append(j+1)
            sum_list = sum(lst)
        gil.append(sum_list)
    print(sum(gil))

"""
["OO","O","OOO"]의 경우 len(num) = 3
따라서 i에 들어갈 수 있는 값은 0,1,2

len(num(i))는 ["OO","O","OOO"]에 있는 요소들의 길이.
"OO"의 경우 len=2 따라서, j에 올수 있는 값은 0,1
하지만 문제에서 주어진 "OO"은 1+2 임.
따라서 j에 1을 더해준다. 

그런데 이렇게 하게 되면 lst = []에 들어오는 것은
[[1,2],[1],[1,2,3]]이다. 따라서 lst안에 있는 각 리스트들의 
합을 구하면 [3,1,6]. 다시 [3,1,6]을 합한 값인 10을 gil에 append
"""