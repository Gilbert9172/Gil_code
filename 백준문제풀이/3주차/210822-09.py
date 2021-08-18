"""
문제번호 : 4673 

단계 : 함수

제목 : 셀프 넘버

알고리즘 분류 : 수학 / 구현
"""
"""
10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
"""

# 생성할 수 있는 수를 만들고 차집합을 구해보기.

#첫 번째 코드 
lst = []
for i in range(1,10001):    
    if i < 10:
        lst.append(i+i)
    elif 10<=i<100:
        lst.append(i+ i//10 + i%10)
    elif 100<=i<1000:
        lst.append(i+ i//100 + (i%100)//10 + ((i%100)%10)//1)
    elif 1000<=i<10000:
        lst.append(i + i//1000 + (i%1000)//100 + ((i%1000)%100)//10 + (((i%1000)%100)%10)//1)


for i in range(1,10001):
    if i not in lst:
        print(i)


# 두 번째 코드
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
