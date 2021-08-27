"""
문제번호 : 11720

단계 : 	문자열

제목 : 숫자의 합

문제 : N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

알고리즘 분류 : 수학/문자열/사칙연산.
"""

N = int(input())

for i in range(1):
    data = input()
    plus = sum(map(int,data))

print(plus)

# ???의 코드 
N = input()
print(sum(map(int,input())))
