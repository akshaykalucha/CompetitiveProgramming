# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


x = int(input())
if x%4 == 1:
    print("0 A")
elif (x+1)%4==1:
    print("1 A")
elif (x+2)%4==1:
    print("2 A")
elif (x+1)%4==3:
    print("1 B")
elif (x+2)%4==3:
    print("2 B")
elif (x+1)%4==2:
    print("1 C")
elif (x+2)%4==3:
    print("2 C")
elif (x+1)%4==0:
    print("1 D")
elif (x+2)%4==0:
    print("2 D")