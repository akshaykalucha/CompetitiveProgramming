# import sys
# sys.stdout = open('DSA/Stacks/output.txt', 'w')
# sys.stdin = open('DSA/Stacks/input.txt', 'r')


import math 
def nextPerfectSquare(N):
    nextN = math.floor(math.sqrt(N)) + 1
    return nextN * nextN

def checkperfectsquare(x):
    if (math.ceil(math.sqrt(n)) == math.floor(math.sqrt(n))):
        return True
    else:
        return False
    
for _ in range(int(input())):
    n = int(input())
    if checkperfectsquare(n):
        print(int(n**0.5),1)
    else:
        zz = nextPerfectSquare(n)
        rc = int(zz**0.5)
        start = zz-(rc*2)+2
        if n < zz-rc:
            col = rc
            row = 0
            for i in range(rc):
                if start+i==n:
                    row = i
                    break
            print(row+1,col)
        else:
            row = rc
            col = 1
            for i in range(rc+1):
                if zz-i==n:
                    col = i
                    break
            if col+1>row:
                print(row-1, col)
            else:
                print(row, col+1)