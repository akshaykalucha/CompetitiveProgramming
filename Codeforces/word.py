str1 = input()
lower = 0
upper = 0
for i in range(len(str1)):
    if str1[i].islower():
        lower+=1
    else:
        upper+=1
if lower >= upper:
    print(str1.lower())
else:
    print(str1.upper())