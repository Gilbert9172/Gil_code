"""
문제 : 상하좌우
"""
# 나의 코드 
N = int(input())

A = input().split()

x,y = 1,1
for i in A:

    if i == 'R':
        x = x 
        y = y + 1

    elif i == 'U':
        x = x + (-1)
        y = y
        if x == 0:
            x = x + 1
            y = y
        else:
            x = x
            y = y

    elif i == 'D':
        x = x + 1
        y = y

    elif i == 'L':
        x = x
        y = y + (-1)

print(x,y)

# N : 크기를 나타낸다 (1<= N <= 100)
# n = int(input())
# x,y = 1,1
# plans = input().split()

# # LURD에 따른 이동 방향
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
# move_types = ['L','R','U','D']

# # 이동 계획을 하나씩 확인
# for plan in plans:
#     #이동 후 좌표 구하기
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]

#     # 공간을 벗어나는 경우 무시
#     if nx < 1 or ny < 1 or nx>n or ny > n:
#         continue
    
#     # 이동 수행
#     x,y = nx,ny

# print(nx,ny)

