
# Code 1
n = input()

lst = []
for i in n:
    try:
        if 65 <= ord(i) <= 90:
            lst.append(i)
    except:
        pass

print("".join(lst))

# Code 2 

n = n.split('-')
for i in n:
    print(i[0])