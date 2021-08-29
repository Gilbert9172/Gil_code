"""
문제 번호 : 2675
단계 : 문자열
제목 : 문자열 반복
알고리즘 : 구현
"""

# 문제 
"""
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.

즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. 

S에는 QR Code "alphanumeric" 문자만 들어있다.

QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
"""


import sys

# 테스트 케이스의 개수 T
T = int(sys.stdin.readline())

for i in range(T):
    data = list(sys.stdin.readline().split())
    
    # 테스트 케이스는 반복 횟수
    R = int(data.pop(0))

    # 문자열 S
    S = data[0]

    lst = []
    for j in range(len(S)):
        lst.append(S[j]*R)

    print("".join(lst))


"""
오늘의 배움 : "".join()

문제를 풀면서 떨어져있는 문자열끼리 합치고 싶었다.
첨에는 for문을 통해서 lst[0]+lst[1]+lst[3]을 시도 했지만 실패
구글에 list concat, list merge 라는 key word로 검색을 해보니
"".join() 함수가 설명 된 부분이 있었다.

"".join() 함수는 리스트의 문자열 요소를 하나로 이어 붙혀준다.
""사이에는 구분자가 들어갈 수 있다.
+ join의 반대는 split이다.


Ex1)
lst = ['I','am','hungry'] 가 있다고 하면, 
print(" ".join(lst))
>>> 'I am hungry' 

Ex2) 정수를 시간으로 바꾸기
lst = ['10','10','15'] 
print(":".join(lst))
>>> '10:10:17'

"""