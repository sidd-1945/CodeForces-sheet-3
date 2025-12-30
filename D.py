a = int(input())
lis = list(map(int,input().split()))
for i in range(0,len(lis)):
    if lis[i] <= 10:
        print(f"A[{i}] = {lis[i]}")