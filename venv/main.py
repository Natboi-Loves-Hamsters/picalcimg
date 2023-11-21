with open('pi100000.dat') as f:
    lpi = f.readlines()
for pi in lpi:
    continue
pi = pi[2:]

vpi = ""
for digit in pi:
    if digit == '0':
        vpi += ("░")
    else:
        vpi += ("█")

print(vpi)