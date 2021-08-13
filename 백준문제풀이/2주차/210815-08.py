# 더하기 사이클 (푸는 중 -> 스터디 때 같이)

"""
99 >= x >= 0 

먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두자리로 만든다.
그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪾 자리수를
"""

"""
정수 N의 앞자리 수 : N[0]
정수 N의 뒷자리 수 : N[-1]

새로 생성되는 숫자 : N1 = N[0]+N[-1]
새로 생성되는 숫자의 뒷자리 : N1[-1]

또 생성되는 숫자 : N = N[-1]*10 + N1[-1]
"""

N = input()
n = int(N)

if n < 10:
    n1 = int(N) * 11
else:
    n1 = int(N[-1])*10 + int(str(int(N[0])+int(N[-1]))[-1])

count=1
while n1 != n:
    n1 = int(str(n1)[-1])*10 + int(str(int(str(n1)[0])+int(str(n1)[-1]))[-1])
    count += 1

    if n1 < 10:
        n1 = n1 * 11
        count += 1
        continue

    elif n1 == n:
        break
    

print(count)




