for _ in range(int(input())):
    #hello
    keyboard = input()
    word = input()
    if len(word) == 1:
        print(0)
    else:
        s = 0
        for i in range(1, len(word)):
            s+=abs((keyboard.index(word[i])+1)-(keyboard.index(word[i-1])+1))
        print(s)