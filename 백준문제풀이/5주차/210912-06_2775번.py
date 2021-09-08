"""
문제번호 : 10250
단계 : 	기본 수학1
제목 : 부녀회장이 될테야  
알고리즘 분류 : 수학
"""

# [풀이 순서]
#1. 0층은 i호에 i명이 거주하기 때문에 [1,2,3...]이다.
#2. 또 k층의 n호 거주 인원은 k-1층의 1,2,...n호 거주인원의 총합이다.
#3. 여기서 모든 층의 1호는 1명이 거주한다는 규칙을 찾을 수 있다.
#4. while문을 사용, 반복 횟수가 층수와 같아질 때 while문 탈출
#5. 리스트의 N-1 번째 출력 (list요소는 0번 부터 시작 but 호수는 1호부터 시작)

T = int(input())

for _ in range(T):
    K = int(input())
    N = int(input())

    floor = [i for i in range(1,N+1)]   #1
    
    count = 0
    while True:
        floor = [sum(floor[0:i]) for i in range(1,len(floor)+1)]    #2
        count += 1
        if count == K:  #4
            break

    print(floor[N-1])   #5