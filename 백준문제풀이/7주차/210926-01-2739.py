# 2739번 : 구구단
# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.
# N은 1보다 크거나 같고, 9보다 작거나 같다.

N = int(input())

count = 0
while 1 <= N <= 9:
    count += 1
    multi = N*count
    print (f'{N} * {count} = {multi}')

    if count==9:
        break
