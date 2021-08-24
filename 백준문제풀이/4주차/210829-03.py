"""
문제 번호 : 10809
단계 : 문자열
제목 : 알파벳 찾기
알고리즘 : 구현, 문자열
"""

# 문제 
"""
알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 
단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 
포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
"""


eng = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

N = input()

data = list(map(str,N))

for i in range(len(eng)):
    if eng[i] in data:
        print(data.index(eng[i]))
    else:
        print(-1)


# ???의 코드
import sys

word = sys.stdin.readline().rstrip()

ans = []
for i in range(97, 123):
    w = chr(i)
    ans.append(str(word.find(w)))

print (" ".join(ans))