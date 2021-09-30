n,m = map(int,input().split())

if n > m:
    lst = [i for i in range(m+1,n)]
    print(len(lst),*lst,sep="\n")

elif n < m:
    lst = [i for i in range(n+1,m)]
    print(len(lst),*lst,sep="\n")

else:
    print(0)
