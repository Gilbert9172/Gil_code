
# Built-In function X 

def test(array):
    lst = [array[i]-array[i-1] for i in range(1,len(array)-1)]
    if len(list(set(lst))) == 1:
        if lst[0] == 1:
            ans =  'ascending'
        elif lst[0] == -1:
            ans = 'descending'
    else:
        ans = 'mixed'
    return ans

array = list(map(int,input().split()))
print(test(array))