a = int(input())
lis1 = list(map(int,input().split()))
b = lis1.copy()
lis1.reverse()
if lis1 == b:
    print("YES")
else:
    print("NO")    