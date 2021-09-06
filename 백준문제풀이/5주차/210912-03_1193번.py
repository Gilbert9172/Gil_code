"""
문제번호 : 1193
단계 : 	기본 수학1
제목 : 분수찾기
알고리즘 분류 : 수학 / 구현
"""

# 홀수 라인 : 분모 감소, 분자 증가
# 짝수 라인 : 분모 증가, 분자 감소  

x = int(input())

line = 1 

while x > line:
    x -= line
    line += 1
    print(x,line)

# line이 짝수인 경우
if line %2 == 0:
    a = x
    b =line - x +1
# line이 홀수인 경우
else:
    a = line - x +1
    b = x

print(f'{a}/{b}')

# 문제 풀이
"""
변수 x가 line 수보다 작아질 때, 
해당하는 대각선에 찾고 있는 변수 x가 있는 것

참고링크 : https://luke-computer.tistory.com/9
"""