a,b = map(int, input().split())
lis = list(map(int,input().split()))
lis.sort()
for i in range(0,b):
    c = int(input())
    start = 0
    end = len(lis)-1
    flag = False
    while start <= end:
        mid = (start + end)//2
        if c == lis[mid]:
            print("found")
            flag = True
            break
        elif c < lis[mid]:
            end = mid - 1
        else:
            start = mid + 1
    if not flag:
        print("not found")             

    