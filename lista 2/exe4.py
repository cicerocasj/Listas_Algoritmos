p1 = float(input('Nota P1: '))
p2 = float(input('Nota P2: '))
p = (p1 + 2*p2)/3
ep1 = float(input('Nota EP1: '))
ep2 = float(input('Nota EP2: '))
ep = (ep1 + 2*ep2)/3
if p >= 6 and ep >= 6:
    mf = (2*p + ep)/3
else:
    mf = min(ep,p)
print('MF = %.2f' %mf)