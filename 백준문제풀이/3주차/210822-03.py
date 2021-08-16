"""
문제번호 : 2577

제목 : 1차원 배열 / 숫자의 갯수

알고리즘 분류 : 수학 / 사칙연산

문제
세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 

각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 

계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.
"""
# 나의 풀이
A = int(input())
B = int(input())
C = int(input())
num = str(A*B*C)

for i in range(10):
    i = str(i)
    N = num.count(i)
    print(int(N))

# 다른 사람 풀이 => ????무슨 뜻인지 해석해야함
n = int(input()) * int(input()) * int(input())
cnt = [0] * 10                 # len이 10인 빈 리스트 만들기.

while n > 0:
    cnt[n%10] = cnt[n%10]+1
    n = n//10

for i in range(10):
    print(cnt[i])