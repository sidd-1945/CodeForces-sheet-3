a = int(input())
lis = list(map(int,input().split()))
ma = max(lis)
mi = min(lis)
for i in range(0,len(lis)):
    if lis[i] == ma:
        lis[i] = mi
    elif lis[i] == mi:
        lis[i] = ma
for next in lis:
    print(next,end=" ")            