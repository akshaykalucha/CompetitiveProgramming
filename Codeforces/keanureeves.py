# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

n = int(input())
ll = input()
zz = set(ll)
if len(zz)==1:
    print(1)
    print(ll)
else:
    ones = ll.count("1")
    zeros = ll.count("0")
    if ones!=zeros:
        print(1)
        print(ll)
    else:
        print(2)
        print(ll[:-1],ll[-1])