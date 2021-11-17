# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

a = 0
b = 0

for _ in range(int(input())):
    mi, ci = map(int, input().split())

    if mi > ci:
        a+=1
    elif ci>mi:
        b+=1
    
if a > b:
    print("Mishka")
elif b> a:
    print("Chris")
else:
    print("Friendship is magic!^^")
        