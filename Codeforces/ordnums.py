# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    if n < 10:
        print(n)
    else:
        c = 9*len(str(n))
        i = 0
        last = int("9"*len(str(n)))
        num = int("1"*len(str(n)))
        while last >n:
            last -= num
            i+=1
        print(c-i)
        