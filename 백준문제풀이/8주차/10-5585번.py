#〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓#
m = int(input())
changes = 1000-m

count = 0 
while changes > 0:
    if 1000> changes >= 500:
        changes -= 500
        count += 1
    elif 500 > changes >=100:
        changes -= 100
        count += 1
    elif 100 > changes >= 50:
        changes -= 50
        count += 1
    elif 50 > changes >= 10:
        changes -= 10
        count += 1 
    elif 10 > changes >= 5:
        changes -= 5
        count += 1
    elif 5>= changes >=1:
        changes -=1
        count +=1
print(count)


#〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓#
changes=1000-m
count=0
for i in [500,100,50,10,5,1]:
    count += (changes//i)       
    changes %= i                # ex. 620%500 = 120, 120%100 = 20, 20%50 = 20, 20%10 = 0, 1%5 = 0
print(count) 