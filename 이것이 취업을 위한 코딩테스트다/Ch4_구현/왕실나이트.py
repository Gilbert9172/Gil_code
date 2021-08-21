"""
실전문제 : 왕실나이트
난이도 : 1 
"""

# 나이트가 해당 포지션에서 이동할 수 있는 경우의 수
# a1에 있을 경우 두 가지 경우 밖에 없다.

# 좌표 평면상에 임의의 점이 주어졌을 때 나이트가 움직일 수 있는 경우의 수를 나타내는 코드

# 현재 나이트의 위치 입력 받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]))-int(ord('a'))+1


# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인

count = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 +1 
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        count += 1

print(count)

"""
알게 된 점

1. ord
문자의 유니코드 값을 돌려 주는 함수 -> 좌표 문제에서 유용할 듯
추가 적으로 ord함수의 반대 함수는 chr()


2. 좌표문제의 경우
리스트를 사용하여 이동할 방향을 기록한다.
또는 위 문제와 같이 steps라는 변수에 이동 방향을 기록한다.
이 두 방법이 자주 사용된다.

3. map(f, iterable)
map 함수는 함수(f)와 반복 가능한(iterable)자료형을 입력으로 받는다.
"""