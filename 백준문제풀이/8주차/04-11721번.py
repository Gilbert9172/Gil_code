#1. 10글자를 끊어서 읽기
#2. 슬라이싱, 리스트


k = input()
p = len(k)//10 + 2

for i in range(1,p):
    print(k[(i-1)*10:i*10])

