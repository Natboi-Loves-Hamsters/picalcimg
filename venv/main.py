import os
import textwrap

wrap = 4

with open('pi250000.dat') as f:
    lpi = f.readlines()
for pi in lpi:
    continue
pi = pi[2:]

palist = [[],[],[],[]]
curarnum = 0
# ialist = [['1','0','0','1'],['0','0','0','0'],['1','0','0','1',],['0','1','1','0']]
ialist = [['0','1','1','1'],['1','1','0','0'],['1','1','1','1'],['0','1','0','1']]
piplace = 0
imglist = []

for digit in pi:
    if len(palist[3]) <= (wrap-1):
        palist[3].append(digit)
        piplace += 1
    if len(palist[3]) == (wrap):
        if len(palist[2]) != (wrap):
            palist[2] = palist[3]
            palist[3] = []
        if len(palist[1]) != (wrap):
            palist[1] = palist[2]
            palist[2] = []
        if len(palist[0]) != (wrap):
            palist[0] = palist[1]
            palist[1] = []
    if ialist == palist:
        print(piplace, palist)
        imglist.append(piplace)
    if len(palist[0]) == wrap and len(palist[1]) == wrap and len(palist[2]) == wrap and len(palist[3]) == wrap:
        palist[0] = palist[1]
        palist[1] = palist[2]
        palist[2] = palist[3]
        palist[3] = []

piplace = 0
print("Printing")
vpi = ""
for digit in pi:
    if piplace < imglist[0]:
        if digit == '0':
            vpi += ("░")
        else:
            vpi += ("█")
        piplace += 1

print('\n'.join(textwrap.wrap(vpi[0 : imglist[0]], 4)))