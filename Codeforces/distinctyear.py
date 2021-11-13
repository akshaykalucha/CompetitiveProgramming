def isUniq(year):
    year = str(year)
    for el in year:
        if year.count(el) > 1:
            return False
    return True
ll = int(input())
while True:
    ll += 1
    if isUniq(ll):
        break
print(ll)