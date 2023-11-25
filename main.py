
"""
TO DO:
    --> Get logical help (stackoverflow would work)
    --> Optimize code
    Add gui (Not a full rewrite but will require a lot of reworking)
    Check through all the wrap possibilities (WILL BE EXTREMELY PAINFUL AND REQUIRE FULL REWRITE OF CODE)
    DO THIS IN A BETTER LANGUAGE (Impossible)
    Adapt into a video game (huh?)
    Figure out why x = y - 1 sometimes equals -y? (this is weird)

"""

import textwrap
from picalc import piGen

DIGITS = int(input("How many digits of pi?: "))

# asks if you want to make pi
unsolved = True
pigenon = bool
while unsolved:
    initpigen = input("Do you wish to generate pi? (Y or N): ")

    if initpigen == 'y' or initpigen == 'Y':
        pigenon = True
        unsolved = False
    if initpigen == 'n' or initpigen == 'N':
        pigenon = False
        unsolved = False
unsolved = True

if pigenon:
    cont = True
    while unsolved:
        save = input("Do you wish to save pi? (Y or N): ")
        if save == 'y' or save == 'Y':
            save = True
            while unsolved:
                cont = input("Do you wish to find the image? (Y or N): ")
                if cont == 'y' or cont == 'Y':
                    cont = True
                    unsolved = False
                if cont == 'n' or cont == 'N':
                    cont = False
                    unsolved = False
        if save == 'n' or save == 'N':
            save = False
            unsolved = False
            
    pi = piGen(DIGITS)
    pi = pi[2:]
    if not cont:
        exit(2)

else:
    # opens pi file and assigns it to pi
    DIGITS = str(DIGITS)
    with open(f'pi{DIGITS}.dat') as f:
        lpi = f.readlines()

    pi = lpi[0]
    pi = pi[2:]

# sets wrap, and hopefully length soon. also make this accord to user input
wrap = 4
length = 4

# sets the length to which palist will fill
palist = []


# setting variables and the actual image
curarnum = 0
# ialist = ['1001','0000'],'1001','0110']
ialist = ['0111', '1100', '1111', '0101']
piplace = 0
imglist = []
piwrap = ""
totaldigit = len(pi)

# This is the sub-optimized code that cycles through pi and assigns it to arrays
for digit in pi:
    piplace += 1
    if len(piwrap) < wrap:
        piwrap += digit
        if (len(piwrap) == wrap) or (piplace == totaldigit):
            palist.append(piwrap)
            piwrap = ""
# This is what checks if it is equal to the image then adds the place it's at to another damn array
piplace = 0
tpip = wrap * (length - 1)
totaldigit = len(palist)
for digit in pi:
    pilist = []
    lenint = piplace
    while (lenint < (length + piplace)) and (lenint < totaldigit):
        pilist.append(palist[lenint])
        lenint += 1
    piplace += 1
    tpip += wrap
    if ialist == pilist:
        print(tpip, pilist)
        imglist.append(tpip)

if len(imglist) == 0:
    print("There is no image in this variation of pi. But here is visualized pi anyways.")
    imglist.append(tpip+300)

# constants and a print
imglnum = 0
piplace = 0
print("Printing")
vpi = ""

# this decides how much of the start and end text you need
starttext = "START"
endtext = "END"
if len(starttext) < wrap:
    starttext += " " * (wrap - len(starttext))
elif len(starttext) != wrap:
    d = wrap - len(starttext)
    starttext = starttext[:d]
if len(endtext) < wrap:
    endtext += " " * (wrap - len(endtext))
elif len(endtext) != wrap:
    d = wrap - len(endtext)
    endtext = endtext[:d]

# This processes the 1s and 0s to the image
for digit in pi:
    if digit == '0':
        vpi += "░"
    else:
        vpi += "█"
    piplace += 1
    # And this here puts the START and END where the images start and end
    if piplace == imglist[imglnum] - wrap * length:
        vpi += starttext
    if piplace == imglist[imglnum]:
        vpi += endtext
        if len(imglist) - 1 > imglnum:
            imglnum += 1

# Finally for the only good bit, the print function. It wraps it by the wrap that is set
print('\n'.join(textwrap.wrap(vpi, wrap)))
