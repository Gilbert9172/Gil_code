# 1이 될 때까지 / 난이도(하) 

"""
어떤 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여
수행 하려고 한다. 단, 두 번째 연산은 N이 K로 나누어 떨어지 때만 선택할 수 있다.
1. N에서 1을 뺀다.
2. N을 K로 나눈다.
"""

n,k = map(int, input().split())
count = 0
# n이k이상이라면 계속 반복.
while n >= k:
    while n%k != 0:         # n이 k의 가 배수가 아니라면 반복.
        n -= 1
        count += 1
    n = n/k
    count += 1

while n > 1:
    n -= 1
    count += 1

print(count)

# 다른 코드

n,k = map(int, input().split())
count = 0

while True:
    target = (n//k)*k
    count += (n-target)
    n = target

    # n이k보다 작을 때 반복문 탈출
    if n < k:
        break
    count += 1
    n //= k