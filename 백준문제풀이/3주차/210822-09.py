"""
문제번호 : 4673 

단계 : 함수

제목 : 셀프 넘버

알고리즘 분류 : 수학 / 구현
"""
"""
10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
"""

# 우선 생성을 할 수 있는 함수를 만들기.
def d(n):
    n = n + sum([int(i) for i in str(n)])     # 각 자리수 더하기 
    return n

range = list(range(1,10001))

lst = []
for i in range:
    lst.append(d(i))

for i in range:
    if i not in lst:
        print(i)


# 각 자리수 더하기 (구글링)
"""
map(int,str(n)) ; 각 자리숫자를 더하기.
"""