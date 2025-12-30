# Replace every positive number by 1.
# Replace every negative number by 2.

a = int(input())
lis = list(map(int,input().split()))
for i in range(0,len(lis)):
    if lis[i] < 0:
        lis[i] = 2
    elif lis[i] > 0:
        lis[i] = 1
for next in lis:
    print(next,end = ' ')                