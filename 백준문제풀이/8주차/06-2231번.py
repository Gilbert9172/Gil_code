n = int(input())

for i in range(1,n+1):
    k = i + sum([int(j) for j in str(i)]) 

    if k == n:
        print(i)
        break
else:
    print(0)
