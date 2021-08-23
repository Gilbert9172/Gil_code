"""
문제번호 : 11654 

단계 : 	문자열

제목 : 아스키 코드

알고리즘 분류 : 구현
"""

# ord(문자) : 아스키 코드를 반환 해준다.
# chr(숫자) : 숫자에 맞는 아스키 코드를 반환해 준다.

# 코드 (정규표현식 사용)
import re 
p = re.compile('[a-zA-Z0-9]')  
N = input()
m = p.match(N)
if m:
    print(ord(N))
else:
    print('No match')