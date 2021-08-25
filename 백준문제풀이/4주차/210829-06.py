"""
문제 번호 : 1152
단계 : 문자열
제목 : 단어의 개수
알고리즘 : 구현/문자열

문제
영어 대소문자와 띄어쓰기만으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 
이를 구하는 프로그램을 작성하시오. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.
"""

import sys
N = sys.stdin.readline().split()
print(len(N))



"""
strip함수
문자열 앞과 끝의 공백문자를 제거해주는 함수.

lstrip() : 인자로 받은 문자를 String의 왼쪽에서 제거
rstrip() : 인자로 받은 문자를 String의 오른쪽에서 제거
"""