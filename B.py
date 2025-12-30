a = int(input())
lis = list(map(int,input().split()))
search = int(input())
flag = 0
for i in range(0,len(lis)):
    if lis[i] == search:
        index = i
        flag = 1
        break
if flag == 1:
    print(index)
else:
    print(-1)        