"""
문제 번호 : 1316
단계 : 문자열
제목 : 그룹단어 체커
알고리즘 : 구현 / 문자열

문자
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 

예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 

나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
"""
# 코드_1 (80ms)
N = int(input())

result = 0
for i in range(N):
    word = input()
    if list(word) == list(sorted(word, key=word.find)):  # key=word.find일 경우 원형의 순서 그대로
        result += 1
print(result)

# 코드_2 (72ms)
N = int(input())

result=N
for i in range(N):
    word = input()
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+1:]:
            result -= 1
            break
print(result)

# 코드_3 (76ms)
N = input()

group = 0
for i in range(N):
    word = input()
    result=0
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            word_list = word[j+1:]
            if word_list.count(word[i]):
                result += 1
    if result == 0:
        group += 1
print(group)


"""
오늘의 배운점 : sorted(iterable, *, key=None, reverse=False)
"""
# Sorted 연습
N = 'gilbert'

print(list(N))
# ['g', 'i', 'l', 'b', 'e', 'r', 't']

# 알파벳 순으로 
print(list(sorted(N)))
# ['b', 'e', 'g', 'i', 'l', 'r', 't']

# key=N.find : 원래 입력값의 순서대로 
print(list(sorted(N, key=N.find)))
# ['g', 'i', 'l', 'b', 'e', 'r', 't']

print(list(sorted(N,reverse=True)))
# ['t', 'r', 'l', 'i', 'g', 'e', 'b']

# sorted lambda 연습(dict의 key,value값을 기준으로 정렬)
money = { 
    "백원" : 100,
    "1$" : 1200,
    "10$" : 12000,
    "오천원" : 5000,
    "만원" : 10000,
    "100$" : 120000,
    "오만원" : 50000
}
print(sorted(money.items(),key=lambda x:x[0]))
# [('1$', 1200), ('10$', 12000), ('100$', 120000), ('만원', 10000), ('백원', 100), ('오만원', 50000), ('오천원', 5000)]
print(sorted(money.items(),key=lambda x:x[1]))
# [('백원', 100), ('1$', 1200), ('오천원', 5000), ('만원', 10000), ('10$', 12000), ('오만원', 50000), ('100$', 120000)]
print(sorted(money.items(),key=lambda x : (-x[1],x[0]))) # -는 반대를 의미
# [('100$', 120000), ('오만원', 50000), ('10$', 12000), ('만원', 10000), ('오천원', 5000), ('1$', 1200), ('백원', 100)]

# sorted lambda 연습2 (단어의 길이를 기준으로 정렬)
lst = ['a','qwerr','ab','qetxbxcaf','abc','sadf11111','asdfg22222222']
print(sorted(lst,key=lambda x : len(x)))



# sort를 사용할 경우. 원래 변수로 출력해줘야 한다.
lst.sort(key=lambda x : len(x))
print(lst)

data = [
    ["고구마",25000],
    ["바나나",123232],
    ["파인애플",4500],
    ["감자",3000],
    ["금귤",6000]
]

data.sort(key=lambda x: x[1])
print(data)
data.sort(key=lambda x: x[0])
print(data)