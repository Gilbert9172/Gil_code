"""
문제 번호 : 1157
단계 : 문자열
제목 : 단어 공부
알고리즘 : 구현/문자열

문제
알파벳 대소문자로 된 단어가 주어지면, 
이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
단, 대문자와 소문자를 구분하지 않는다.
"""

# 나의 코드 
# 대소문자를 구분하지 않는다. -> 통일 시켜준다(대문자)
N = input().upper()

# 단어의 알파벳 split
data = set(list(N))
print(data)

# 입력된 값중에서 가장 많은 알파벳 카운트
lst = []
for i in data:
    letters = N.count(i)
    lst.append(letters)
print(lst)

#  문자 list 와 카운트 list zip
zipped_list = set(list(zip(lst,data)))
print(zipped_list)

lst1 = []
for j in zipped_list:
    lst1.append(j[0])

MAX = max(lst1)
MAX_count = lst1.count(MAX)
if MAX_count > 1:
    print("?")
else:
    print(max(zipped_list)[1])




# ???의 코드
word = input().upper()
word_list = list(set(word))

cnt = []
for i in word_list:
    count = word.count(i)
    cnt.append(count)

MAX = max(cnt)
if cnt.count(MAX) > 1:
    print("?")
else:
    print(word_list[(cnt.index(MAX))])
