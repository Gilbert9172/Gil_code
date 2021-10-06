N = int(input())
odd = N - N//2
even = N//2

for _ in range(N):
    print("* " * odd)
    print(" *" * even)