T = int(input())

for _ in range(T):
    K = int(input())
    N = int(input())

    floor = [i for i in range(1,N+1)]

    count = 0
    while True:
        floor = [sum(floor)[0:i] for i in range(1,len(floor)+1)]
        count += 1
        if count == K:
            break

    print(floor[N-1])