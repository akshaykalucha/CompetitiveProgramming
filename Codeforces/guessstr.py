for _ in range(int(input())):
    s = input()
    if len(s) == 2:
        print(s)
    else:
        ans = f"{s[0]}{s[1]}"
        ll = s[2:]
        i = 1
        while i <= len(s)-2:
            ans+=ll[i]
            i+=2
        print(ans)