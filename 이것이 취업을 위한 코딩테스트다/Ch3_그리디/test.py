n,k = map(int, input().split())
count = 0

if n%k == 0:

    while True:
        n = n/k
        count += 1

print(n, count)