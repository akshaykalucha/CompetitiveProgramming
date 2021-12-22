# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    ss = input()
    pp = input()
    vov = "aeiou"
    if ss==pp:
        print(0)
    else:
        alphs = [chr(i) for i in range(97,123)]
        orops = 9999999999
        for j in range(len(alphs)):
            aa = ss
            bb = pp
            aa = aa.replace("?",alphs[j])
            bb = bb.replace("?",alphs[j])
            ops = 0
            for i in range(n):
                if aa[i]==bb[i]:
                    continue
                if aa[i] in vov and bb[i] not in vov:
                    ops+=1
                elif aa[i] not in vov and bb[i] in vov:
                    ops+=1
                else:
                    ops += 2
            orops = min(orops,ops)
            if orops==0:
                break
        print(orops)