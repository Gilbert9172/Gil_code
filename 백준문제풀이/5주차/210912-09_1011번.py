"""
문제번호 : 1011
단계 : 	기본 수학1
제목 : Fly me to the Alpha Centauri
알고리즘 분류 : 수학
"""

# import math
# for _ in range(int(input())):
#     x, y = map(int, input().split())
#     print(math.ceil(2 * math.sqrt(y - x) - 1))


t = int(input())
for i in range(t):

    a, b = map(int, input().split())
    c = b - a

    num = 1
    while True:
        if num ** 2 <= c < (num + 1) ** 2:
            break
        num += 1
        
    if num ** 2 == c:
        print((num * 2) - 1)
    elif num ** 2 < c <= num ** 2 + num:
        print(num * 2)
    else:
        print((num * 2) + 1)