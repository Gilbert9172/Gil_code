"""
문제 번호 : 5622
단계 : 문자열
제목 : 다이얼
알고리즘 : 구현

문제

전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 
숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 
한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 
각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.
"""

# GIL_Code (너무 별로다... => 내일 새로운 코드 시도 )
N = list(map(str,input().upper()))

lst =[]
for i in N:
    
    if i == 'A' or i == 'B' or i == 'C':
        lst.append(3)

    elif i =='D' or i =='E' or i =='F':
        lst.append(4)

    elif i =='G' or i =='H' or i =='I':
        lst.append(5)

    elif i =='J' or i =='K' or i =='L':
        lst.append(6)

    elif i =='M' or i =='N' or i =='O':
        lst.append(7)

    elif i =='P' or i =='Q' or i =='R' or i =='S':
        lst.append(8)

    elif i =='T' or i =='U' or i =='V':
        lst.append(9)

    elif i =='W' or i =='X' or i =='Y' or i =='Z':
        lst.append(10)

print(sum(lst))

#