"""
문제번호 : 5596
단계 : 	Bronze4
제목 : 시험 점수
알고리즘 분류 : 수학/구현/사칙연산
"""
#1
import sys 

lst = []
for i in range(2):
    data = sum(map(int,sys.stdin.readline().split()))
    lst.append(data)

if lst[0]==lst[1]:
    print(lst[0])
else:
    print(max(lst))

#2
x = sum(map(int,input().split()))
y = sum(map(int,input().split()))
print(max(x,y))