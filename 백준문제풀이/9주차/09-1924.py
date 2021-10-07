# bulit-in X
date = 0
x,y = map(int,input().split())
for month in range(1,x):
    if  month in (1,3,5,7,8,10,12):
        date += 31
    elif month == 2:
        date += 28
    elif month in (4,6,9,11):
        date += 30

days= ['SUN','MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

ans = (date+y) % 7

print(days[ans])


# bulit-in O
import calendar

days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
x, y = map(int, input().split())

day = calendar.weekday(2007, x, y) # 0:월욜, 1:화욜, 2:수욜...

print(days[day])