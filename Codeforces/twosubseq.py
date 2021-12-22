# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    ss = input()
    z = ss
    z = list(z)
    z.sort()
    first = z[0]
    for i in range(len(ss)):
        if ss[i]==z[0]:
            print(first, ss[:i]+ss[i+1:])
            break