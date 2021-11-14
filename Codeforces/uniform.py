n = int(input())
home = []
guest = []
for i in range(n):
    th, tg = map(int, input().split())
    home.append(th)
    guest.append(tg)
c= 0
for i in range(len(home)):
    color = home[i]
    for j in range(len(guest)):
        if color == guest[j] and j!=i:
            c+=1
print(c)