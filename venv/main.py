import os
import textwrap

wrap = 4



with open('pi100000.dat') as f:
    lpi = f.readlines()
for pi in lpi:
    continue
pi = pi[2:]

palist = [[],[],[],[]]
curarnum = 0
ialist = [['0','1','1','1'],['1','1','0','0'],['1','1','1','1'],['0','1','0','1']]
running = True
piplace = 0

while running:
    if palist != ialist:
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
                running = False
            elif len(palist[0]) == wrap and len(palist[1]) == wrap and len(palist[2]) == wrap and len(palist[3]) == wrap:
                palist[0] = palist[1]
                palist[1] = palist[2]
                palist[2] = palist[3]
                palist[3] = []

vpi = ""
for digit in pi:
    if digit == '0':
        vpi += ("░")
    else:
        vpi += ("█")
print('\n'.join(textwrap.wrap(vpi[0 : piplace], 4)))