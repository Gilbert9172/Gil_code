# 더하기 사이클 (푸는 중)

"""
99 >= x >= 0 

먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두자리로 만든다.
그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪾 자리수를
"""
# a = '14'
# print(a[1])

# b = int(a[0])+int(a[1])
# print(b)

# c = (int(a[1])*10)+b
# print(c)


# N의 뒷자리 : N[-1]
# "N의 각 자리수의 합"의 뒷자리 : (N[0]+N[-1])[-1]

# 새로운 숫자 : ( N[-1]*10 ) + (N[0]+N[-1])[-1]

# new_num == N -> break

N = int(input())

count = 0
# while True:
#     # while N < 10:
#     #     N *= 10

#     n = str(N)
#     n1 = (int(n[-1])*10) + int((n[0]+n[-1])[-1])
#     count += 1
#     if N == n1:
#         break
# print(count)
while True:
    try:
        n = str(N)
        n1 = (int(n[-1])*10) + int((n[0]+n[-1])[-1])
        if n1 == N:
            count += 1
    except:
        break