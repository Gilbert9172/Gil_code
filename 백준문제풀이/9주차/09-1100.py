# 체스판
#1 ■□■□■□■□
#2 □■□■□■□■
#3 ■□■□■□■□
#4 □■□■□■□■
#5 ■□■□■□■□
#6 □■□■□■□■
#7 ■□■□■□■□
#8 □■□■□■□■

import sys
chess = [sys.stdin.readline().strip() for i in range(8)]

count = 0
for i in range(len(chess)):
    if i%2 == 0:
        for j in range(0,7,2):
            if chess[i][j] == 'F':
                count += 1

    elif i%2 == 1:
        for j in range(1,8,2):
            if chess[i][j] == 'F':
                count += 1

print(count)
