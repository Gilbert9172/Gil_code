color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

data = [input() for _ in range(3)]

a = color.index(data[0])
b = color.index(data[1])
c = 10**(color.index(data[2]))

ans = (a*10 + b) * c

print(ans)
