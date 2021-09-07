"""
문제번호 : 10250
단계 : 	기본 수학1
제목 : ACM 호텔
알고리즘 분류 : 수학 / 구현 / 사칙연산
"""

# 엘레베이터 이동 거리는 신경 쓰지 않는다.
# 엘베에서 가까운 방 선호
# H(호텔의 층수), W(각 층의 방수), N(몇 번째 손님인지)

# Y,YY : 호텔 층수
# X,XX : 엘레베이터로 부터 방의 거리

# 예제
"""
2
6 12 10 -> 6층 / 12개의 객식 / 10번째 손님의 방호수는?
30 50 72
"""
T = int(input())

lst=[]
for i in range(T):
    H,W,N = map(int,input().split())

    count = 1
    while True:

        if H*W < N:
            break

        N -= H
        count += 1
        # print(N,H,count)

        if N <= H and N != 0:
            # print(f'{N}0{count}')
            print((N*100)+count)
            break


##
num = int(input())

for i in range(num):
    H, W, N = map(int, input().split())
    floor = N % H
    room = N // H + 1
    if floor == 0: # 가장 꼭대기 
        room -= 1  
        floor = H

    print(floor*100 + room)