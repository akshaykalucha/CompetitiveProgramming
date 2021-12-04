# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    s = list(input())
    turn = 0
    for i in range(len(s)):
        if turn == 0:
            if s[i]=="a":
                s[i]="b"
            else:
                s[i]="a"
            turn = 1
        elif turn == 1:
            if s[i]=="z":
                s[i]="y"
            else:
                s[i]="z"
            turn = 0
    print("".join(s))