c = 0
for _ in range(int(input())):
    ss = input()
    if ss == "++X" or ss == "X++":
        c += 1
    else:
        c-=1
print(c)