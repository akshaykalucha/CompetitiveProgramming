# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ll = list(input())
    n=len(ll)
    i = 0
    if n==1:
        print(ll[0]+ll[0])
    else:
        if ll[1]>=ll[0]:
            print(ll[0]+ll[0])
        else:
            while i<=n-2:
                if ll[i]<ll[i+1]:
                    break
                elif ll[i+1]<ll[i]:
                    i+=1
                elif ll[i+1]==ll[i]:
                    for j in range(i+1,n):
                        if ll[j]>ll[i]:
                            break
                        elif ll[j]<=ll[i]:
                            i=j
                            continue
            mystr="".join(ll[:i+1])
            print(mystr+mystr[::-1])