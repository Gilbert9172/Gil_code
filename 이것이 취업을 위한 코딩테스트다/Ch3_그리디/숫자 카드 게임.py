# 숫자 카드 게임 / 난이도(하) / 제한시간(30분)


# 나의 코드 => 뭔가 용량이 클거같다.
import sys

# 1. n(행),m(열)값을 입력
n,m = map(int, input().split())

# 2. n이 카드 배치 모양?의 길이가 된다.
# List Comprehension 사용 하여 카트의 배열 입력.
lst = []
for i in range(n):
    data = list(map(int, sys.stdin.readline().rsplit()))
    lst.append(data)

# 3. 카드의 배열 중 가장 작은 값을 뽑아서 List Comprehension 한번 더
# 그리고 그 중에 가장 큰 값을 출력
gil = []
for i in range(len(lst)):
    gil.append(min(lst[i]))

    for j in gil:
        num = max(gil)

print(num)

# 풀이 코드 1
n,m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)                       # 현재 줄에서 '가장 작은 수' 찾기
    result = max(result, min_value)             # '가장 작은 수'들 중에서 가장 큰 수 찾기

# 풀이 코드2 (이중for문)
n,m = map(int,input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001                          # 임의의 값 설정

    for j in data:
        min_value = min(min_value, j) 
    result = max(result, min_value)
print(result)


