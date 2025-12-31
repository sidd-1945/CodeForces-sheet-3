a = int(input())
lis = list(map(int,input().split()))
lis.sort()
l1 = lis.copy()
for next in l1:
    print(next,end=" ")