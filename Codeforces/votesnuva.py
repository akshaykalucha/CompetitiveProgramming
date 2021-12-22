# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

up,down,z = map(int, input().split())
if z==0:
    if up>down:
        print("+")
    elif down>up:
        print("-")
    else:
        print("0")
else:
    if down>z+up:
        print("-")
    elif up>z+down:
        print("+")
    elif z+down>=up or z+up>=down:
        print("?")