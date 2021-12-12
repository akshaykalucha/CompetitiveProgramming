# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        brak = "()"
        if i == 0:
            print(brak*n)
        else:
            open = "("
            close = ")"
            print(open + (open*i)+(close*i) + brak*(n-(i+1))+close)