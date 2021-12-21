# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')

for _ in range(int(input())):
    a,b = map(int, input().split())
    st = 0
    diff = abs(b-a)
    st+=(diff//5)
    diff -= (diff//5)*5
    st+=(diff//2)
    diff -= (diff//2)*2
    st+=(diff//1)
    diff -= (diff//1)*1
    print(st)