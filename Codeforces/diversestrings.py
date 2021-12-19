# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    ll = list(input())
    kk = set(ll)
    if len(kk)!=len(ll):
        print("NO")
    else:
        alph = "".join([chr(i) for i in range(97,123)])
        ll.sort()
        if len(ll)==1:
            print("YES")
        else:
            if "".join(ll) not in alph:
                print("NO")
            else:
                print("YES")