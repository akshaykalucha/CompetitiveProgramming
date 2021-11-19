# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

for _ in range(int(input())):
    n, x = map(int, input().split())
    floor = 1
    appt = 2
    while appt < n:
        appt+=x
        floor+=1
    print(floor)