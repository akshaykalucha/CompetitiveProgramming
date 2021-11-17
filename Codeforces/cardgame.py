# import sys
# sys.stdout = open('Codeforces/output.txt', 'w')
# sys.stdin = open('Codeforces/input.txt', 'r')

n = int(input())
game = list(map(int, input().split()))

s = 0
d = 0
turn = 0
while len(game) > 0:
    maxcard = max(game[0], game[-1])
    if turn == 0:
        s+=maxcard
        turn = 1
    else:
        d+=maxcard
        turn = 0
    game.pop(game.index(maxcard))
print(s, d)