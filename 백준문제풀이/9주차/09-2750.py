n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort()
for i in range(len(lst)):
    print(lst[i])

