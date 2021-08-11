# 큰 수의 법칙
# 난이도 하
# 풀이 시간 30분

# 풀이 1.

# N(), M(M번 더할수 있음), K(같은 수 반복 k번)를 공백으로 구분하여 입력받기
n,m,k = map(int,input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int,input().split()))

data.sort()             # 입력 받은 수를 정렬하기.
first = data[n-1]       # 가장 큰 수
second = data[n-2]      # 두번째로 큰 수

result = 0

while True:
    for i in range(k):  # 가장 큰수를 k번 더하기
        if m==0:        # 더하는 횟수가 0이면 break
            break
        result += first # 가장 큰수 더하기
        m -= 1          # 더해질 때마다 -1
    if m == 0:
        break
    result += second    # 두번째로 큰수 더하기
    m -=1               # 더할 때 마다 -1

print(result)


# 풀이 2.
# 반복되는 수열의 길이 = k+1
# M / (K+1) = 수열이 반복 되는 횟수 ; 나누어 떨어질 경우
# K*(M / (K+1)) = 가장 큰수가 등장하는 횟수.

# 결과적으로 "가장 큰 수가 더해지는 횟수" = int(K*(M/(K+1)))+M%(K+1)

n,m,k = map(int,input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수
count = int(m/(k+1))*k
count += m%(k+1)

result = 0
result += (count)*first         # 가장 큰 수 더하기
result += (m-count)*second      # 두번째로 큰 수 더하기

print(result)
