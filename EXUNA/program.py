t=int(input())
for i in range(0,t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    s=l[0]
    for j in range(1,n):
        s=s%l[j]
    print(s)