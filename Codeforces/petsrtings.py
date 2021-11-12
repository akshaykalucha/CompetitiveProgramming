str1 = input().lower()
str2 = input().lower()

if str1 == str2:
    print(0)
else:
    for i in range(len(str1)):
        # print(ord(str1[i]), ord(str2[i]))
        if ord(str1[i]) < ord(str2[i]):
            print(-1)
            break
        elif ord(str1[i]) > ord(str2[i]):
            print(1)
            break