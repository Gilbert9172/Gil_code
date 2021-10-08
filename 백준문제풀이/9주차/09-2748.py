# for문 사용
n = int(input())

d = [0]*(n+1)

for i in range(n+1):

    if i < 2:
        d[i] = i
    else:
        d[i] = d[i-1] + d[i-2]

print(d[n])

# 재귀함수 사용 → 시간초과
def test(n):
    if n < 2:
        return n
    else:
        return test(n-1) + test(n-2)