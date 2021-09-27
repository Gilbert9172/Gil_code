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
    return max(array)

# 출력
n,m = map(int,input().split())
lst = list(map(int,input().split()))
print(test(lst))


## itertools 사용 

# from itertools import combinations # n길이 만큼의 튜플을 리스트로 반환 / [(a,b),(a,b),(a,b)]

# k,m = map(int,input().split())
# n = list(map(int,input().split()))

# lst = list(combinations(n,3))

# array = [sum(lst[i]) for i in range(len(lst)) if sum(lst[i])<=m]


# print(max(array))