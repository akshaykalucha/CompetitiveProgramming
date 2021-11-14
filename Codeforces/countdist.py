s = input()
s = s.replace("{","")
s = s.replace("}","")
s = s.replace(",","")
s = s.replace(" ","")

if len(s) == 0:
    print(0)
else:
    ll = list(s)
    print(len(set(ll)))