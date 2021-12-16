# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    s = list(input())
    t = input()
    s.sort()
    non = []
    a = s.count('a')
    b = s.count('b')
    c = s.count('c')
    for i in range(len(s)):
        if s[i]!='a' and s[i]!='b' and s[i]!='c':
            non.append(s[i])
    if t=="abc" and a>0 and b>0 and c>0:
        print("a"*a+"c"*c+"b"*b+"".join(non))
    elif t=="bc":
        print("a"*a+"c"*c+"b"*b+"".join(non))
    elif t=="ab":
        print("b"*b+"a"*a+"c"*c+"".join(non))
    elif t=="ac":
        print("c"*c+"a"*a+"b"*b+"".join(non))
    else:
        print("".join(s))