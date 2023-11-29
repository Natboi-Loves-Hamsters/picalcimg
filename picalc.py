"""
TO DO:
    --> Optimize code
    --> Add multiple ialist options (Probably want to put the lists in an array)
    Add gui (Not a full rewrite but will require a lot of reworking)
    Check through all the wrap possibilities (WILL BE EXTREMELY PAINFUL AND REQUIRE FULL REWRITE OF CODE)
    Figure out why x = y - 1 sometimes equals -y? (this is weird)

"""

from main import piGen, piSearch

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

# questions for generating pi after linking the scripts
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

# ialist = ['1001','0000'],'1001','0110']
ialist = ['0111', '1100', '1111', '0101']
piSearch(pi,ialist)