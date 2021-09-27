## for문

n = int(input()) # n>=2
lst = [i for i in range(n+1)]

for i in range(0,len(lst)-2):
    lst[i+2] = lst[i+1]+lst[i]

print(max(lst))


## 재귀함수
def test(n):
    if n <= 1:
        return n
    else:
        return test(n-1) + test(n-2) 

n = int(input())
print(test(n))