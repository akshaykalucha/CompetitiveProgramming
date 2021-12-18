# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


for _ in range(int(input())):
    ll = list(input())
    if len(ll)>=2:
        if ll[-1]=='o' and ll[-2]=='p':
            print("FILIPINO")
        elif ll[-1]=='u' and ll[-2]=='s' and ll[-3]=='e' and ll[-4]=='d':
            print("JAPANESE")
        elif ll[-1]=='u' and ll[-2]=='s' and ll[-3]=='a' and ll[-4]=='m':
            print("JAPANESE")
        elif ll[-1]=='a' and ll[-2]=='d' and ll[-3]=='i' and ll[-4]=='n' and ll[-5]=='m':
            print("KOREAN")