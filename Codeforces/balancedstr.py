# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

for _ in range(int(input())):
    word = input()
    zz = set(word)
    if "B" not in zz:
        print("NO")
    else:
        if "A" in zz and "C" in zz:
            if word.count("A")+word.count("C")==word.count("B"):
                print("YES")
            else:
                print("NO")
        elif "A" in zz and "C" not in zz:
            if word.count("A")==word.count("B"):
                print("YES")
            else:
                print("NO")
        elif 'C' in zz and "A" not in zz:
            if word.count("C")==word.count("B"):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")