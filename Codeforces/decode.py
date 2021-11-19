# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

n = input()
zz = ""
i=0
while i<len(n):
    if i == len(n)-1:
        zz+="0"
        i+=1
    else:
        if n[i]+n[i+1]=="-.":
            zz+="1"
            i+=2
        elif n[i]+n[i+1]=="--":
            zz+="2"
            i+=2
        else:
            zz+="0"
            i+=1
print(zz)