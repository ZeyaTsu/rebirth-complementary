import rebirth

d = rebirth.rand(1, 10)
s = True
while s:
    e = rebirth.guess(d)
    if e == d:
        s = False

