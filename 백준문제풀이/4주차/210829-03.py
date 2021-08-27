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

# 나의 코드
eng = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

N = input()

data = list(map(str,N))

for i in range(len(eng)):
    if eng[i] in data:
        print(data.index(eng[i]))
    else:
        print(-1)

# ???의 코드
import string
N=input()
for a in list(string.ascii_lowercase):
	print(N.find(a),end=' ')

# ???의 코드
N=input()
for i in range(97,122):
    print(N.find(chr(i)))
print(N.find(chr(122)))

"""
오늘의 배움1 : import string

[일반적인 문자열 연산](https://docs.python.org/ko/3/library/string.html?highlight=string#module-string)

strin.ascii_letters : ascii_lowercase + ascii_uppercase 

string.ascii_lowecase : 소문자 'abcdefghijklmnopqrstuvwxyz'

strin.ascii_uppercase : 대문자 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

오늘의 배움2 : find

find(찾을 문자, 찾기 시작할 위치) ; 없는 문자일 경우 -1을 반환

+ startswith(시작하는 문자, 시작할 위치) ; ture , false 반환

+ endswith(끝나는 문자,문자열의 시작, 문자열의 끝) ;  ture , false 반환

"""