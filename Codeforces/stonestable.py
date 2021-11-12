num = int(input())
str1 = input()
if len(str1) == 1:
    print(0)
else:
    c = 0
    for i in range(len(str1)-1):
        if str1[i]==str1[i+1]:
            c+=1
    print(c)