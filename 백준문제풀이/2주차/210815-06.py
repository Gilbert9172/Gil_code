# 10952 / (A+B -5) 

"""
두 정수 A와B를 입력 받은 다음,
A+B를 출력하는 프로그램을 작성하시오.
"""
while True:
    A,B = map(int,input().split())
    if A>0 and B<10:
        plus = A+B
        print(plus)
    else:
        break