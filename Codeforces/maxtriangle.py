# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    w,h = map(int, input().split())
    h1 = list(map(int, input().split()))
    h1.pop(0)
    h2 = list(map(int, input().split()))
    h2.pop(0)
    v1 = list(map(int, input().split()))
    v1.pop(0)
    v2 = list(map(int, input().split()))
    v2.pop(0)
    abh1 = (abs(max(h1)-min(h1)))*h
    abh2 = (abs(max(h2)-min(h2)))*h
    abv1 = (abs(max(v1)-min(v1)))*w
    abv2 = (abs(max(v2)-min(v2)))*w
    print(max([abh1,abh2,abv1,abv2]))