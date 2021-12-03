# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    pos = input()
    zz = ""
    for el in pos:
        if el == "D":
            zz+="U"
        elif el =="U":
            zz+="D"
        else:
            zz+=el
    print(zz)