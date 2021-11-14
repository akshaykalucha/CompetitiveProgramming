n = int(input())
ll = input().lower()
flag = True
al = list(map(chr, range(97, 123)))
for i in range(len(al)):
    if al[i] not in ll:
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")