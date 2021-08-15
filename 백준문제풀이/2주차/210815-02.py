# 15552번 : 빠른 A+B

### 문제
"""
첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 
다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.
"""

### 알고리즘
"""
1단계 : 정수 입력
2딘계 : 두개의 정수가 한줄에 오게끔 만들기
3단계 : 두개의 정수를 더하기
4단계 : 한번에 출력하기.
"""

import sys
n = int(sys.stdin.readline()) 
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    plus = a+b
print(plus)
# 입력
## input()대신 sys.stdin.readline()을 사용하는 이유는?
"""
시간 단축을 위해. 속도순서 (sys.stdin.readline > raw_input() > input())
"""

"""
### 한 라인만 입력 받을 때
num = int(sys.stdin.readline()) 

### readlines => 여러값을 list로 반환해준다.
num = int(sys.stdin.readlines()) 

### 여러 라인 입력 받을 경우
n = input()
a = [sys.stdin.readline() for i in range(n)]
"""