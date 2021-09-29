# 9명의 난쟁이의 키 중 7명의 키 합이 100인

# itertools 
from itertools import combinations

h = [int(input()) for _ in range(9)]

combi = list(combinations(h,7))

lst = [sorted(list(i)) for i in combi if sum(i)==100]

for i in lst:
    print(*i, sep="\n")
    break

# for문
a = [int(input()) for _ in range(9)]
asum = sum(a)
a.sort()

for i in range(9):
    for j in range(i+1,9):
        if asum - a[i] - a[j] == 100:
            [print(a[k]) for k in range(9) if k not in (i,j)]
