n = int(input())
gg = input()
if gg.count("A") > gg.count("D"):
    print("Anton")
elif gg.count('D') > gg.count('A'):
    print("Danik")
else:
    print("Friendship")