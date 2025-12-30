# a = int(input())
# lis = list(map(int,input().split()))
# min = lis[0]
# index = 0
# for i in range(1,len(lis)-1):
#     if min > lis[i]:
#         min = lis[i]
#         index = i
# print(f"{min} {index}")    
 
a = int(input())
lis = list(map(int,input().split()))    
small = min(lis)
for i in range(0,len(lis)):
    if small == lis[i]:
        index = i+1
        break
print(small, index)
