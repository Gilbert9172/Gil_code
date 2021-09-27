#1. 카드 세장의 합을 구한다 → 어떻게? for문 사용하여 slicing으로 
#2. 합을 list에 append해서, max()로 결과 도출


# 구현
def test(lst):
    array = []
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            for k in range(j+1,len(lst)):
                ans = lst[i]+lst[j]+lst[k]
                if ans <= m:
                    array.append(ans)
    return array

# 출력
n,m = map(int,input().split())
lst = list(map(int,input().split()))
print(test(lst))
