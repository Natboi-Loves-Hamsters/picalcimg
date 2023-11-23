'''
TO DO:
    --> Get logical help (stackoverflow would work)
    --> Streamline the palist function and make it not hardcoded to length of 4 (need logical help first)
    Add gui (Not a full rewrite but will require a lot of reworking)
    Check through all the wrap possibilities (WILL BE EXTREMELY PAINFUL AND REQUIRE FULL REWRITE OF CODE)
    DO THIS IN A BETTER LANGUAGE (Impossible for me)
    Adapt into a video game (huh?)
    Figure out why x = y - 1 sometimes equals -y? (this is weird)
'''

import os
import textwrap

# sets wrap, and hopefully length soon. also make this accord to user input
wrap = 4

# opens pi file and assigns it to pi
with open('pi100000.dat') as f:
    lpi = f.readlines()
for pi in lpi:
    continue
pi = pi[2:]

# setting variables and the actual image
palist = [[],[],[],[]]
curarnum = 0
# ialist = [['1','0','0','1'],['0','0','0','0'],['1','0','0','1',],['0','1','1','0']]
ialist = [['0','1','1','1'],['1','1','0','0'],['1','1','1','1'],['0','1','0','1']]
piplace = 0
imglist = []

# This is the horribly optimized code that cycles through pi and assigns it to arrays
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
    # This is what checks if it is equal to the image and adds the place it's at to another damn array
    if ialist == palist:
        print(piplace, palist)
        imglist.append(piplace)
    # This cycles everything up when it is all filled up
    if len(palist[0]) == wrap and len(palist[1]) == wrap and len(palist[2]) == wrap and len(palist[3]) == wrap:
        palist[0] = palist[1]
        palist[1] = palist[2]
        palist[2] = palist[3]
        palist[3] = []

if len(imglist) == 0:
    print("There is no image in this variation of pi. But here is visualized pi anyways.")
    imglist.append(piplace+17)

# This processes the 1s and 0s to the image
imglnum = 0
piplace = 0
print("Printing")
vpi = ""
for digit in pi:
    if digit == '0':
        vpi += ("░")
    else:
        vpi += ("█")
    piplace += 1
    # And this here puts the STRT and END where the images start and end
    if piplace == imglist[imglnum] - 16:
        vpi += ('STRT')
    if piplace == imglist[imglnum]:
        vpi += ('END ')
        if len(imglist) - 1 > imglnum:
            imglnum += 1

# Finally for the only good bit, the print function. It wraps it by the wrap that is set
print('\n'.join(textwrap.wrap(vpi, wrap)))