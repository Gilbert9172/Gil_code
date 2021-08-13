
N = input()
n = int(N)

if n < 10:
    n1 = int(N) * 11
else:
    n1 = int(N[-1])*10 + int(str(int(N[0])+int(N[-1]))[-1])

# n1 = int(str(n1)[-1])*10 + int(str(int(str(n1)[0])+int(str(n1)[-1]))[-1])
# print(n1)
print(n1)
count=1
while n1 != n:
    n1 = int(str(n1)[-1])*10 + int(str(int(str(n1)[0])+int(str(n1)[-1]))[-1])
    count += 1

    if n1 < 10:
        n1 = n1 * 11
        count += 1
        continue

    elif n1 == n:
        print(n1)
        break

print(count)
