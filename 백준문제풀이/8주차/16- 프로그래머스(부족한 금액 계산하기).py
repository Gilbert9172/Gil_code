def solution(price, money, count):
    lst = sum([i*price for i in range(1,count+1)])
    ans = lst-money
    if ans<0:
        return 0
    else:
        return ans

print(solution(3,20,4))