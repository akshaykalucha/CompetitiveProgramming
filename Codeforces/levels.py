t = int(input())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
lst = []
for i in range(1, t+1):
    lst.append(i)
 
for i in range(1, lst1[0]+1):
    if lst1[i] in lst:
        lst.remove(lst1[i])
for i in range(1, lst2[0]+1):
    if lst2[i] in lst:
        lst.remove(lst2[i])
        
if len(lst) == 0:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")