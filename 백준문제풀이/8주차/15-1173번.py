N, m, M, T, R = 5, 70, 120, 25, 15
heart = m
exercise = 0
rest = 0
if m + T > M:
    print(-1)
else:
    while exercise < N:     
        if heart + T <= M:          # 맥박이 최대 맥박보다 낮을 때
            exercise += 1
            heart += T
        elif heart + T > M:
            rest += 1
            heart -= R
            if heart < m:           # 맥박이 최소 맥박보다 낮을 때
                heart = m
    print(exercise+rest)