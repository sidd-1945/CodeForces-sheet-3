a = int(input())
sum = 0
lis = list(map(int,input().split()))
for next in lis:
    sum = sum + next
print(abs(sum))    