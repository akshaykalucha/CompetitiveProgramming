# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

for _ in range(int(input())):
    k = int(input())
    z = []
    i=1
    while len(z) !=k:
        if str(i)[-1]=="3" or i%3==0 or str(i)[-1]=="3" and i%3==0:
            pass
        else:
            z.append(i)
        i+=1
    print(z[-1])