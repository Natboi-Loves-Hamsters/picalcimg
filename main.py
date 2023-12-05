import time
import sys

if sys.platform == "linux" or sys.platform == "linux2":
    sys.set_int_max_str_digits(999999999)

def piGen(DIGITS,save = False,verbose = True,binary = True):

    if not save:
        global pi
    def pi_digits(x):

        k,a,b,a1,b1 = 2,4,1,12,4
        goes = 0
        it = time.time()
        st = it
        totaltime = 0
        while x > 0:
            p,q,k = k * k, 2 * k + 1, k + 1
            a,b,a1,b1 = a1, b1, p*a + q*a1, p*b + q*b1
            d,d1 = a/b, a1/b1
            while d == d1 and x > 0:
                yield int(d)
                x -= 1
                a,a1 = 10*(a % b), 10*(a1 % b1)
                d,d1 = a/b, a1/b1
                goes += 1
                if goes % 1000 == 0 and verbose:
                    ips = time.time() - st
                    totaltime += ips
                    st = time.time()
                    if goes == 1000:
                        ips = 1000 / ips
                        tbf = ips / (x / 1000)
                        tbf = x / tbf
                        tbf *= 1.1
                        if verbose:
                            print(f"Estimated {tbf:.2f} seconds till finish.\n")
                    if verbose:
                        print(f"Elapsed time: {totaltime:.2f} out of {tbf:.2f}")
                        print(f"Percentage finished: {goes / DIGITS * 100:.2f}%\n")
        if verbose:
            print("True time to finish:", time.time() - it)

    digits = [str(n) for n in list(pi_digits(DIGITS))]
    pi = ("%s.%s\n" % (digits.pop(0), "".join(digits)))

    pi = pi[2:]
    pi = int(pi)

    if binary:
        pi = bin(pi)
    else:
        pi = float(pi)

    if save:
        with open(f'pi{DIGITS}.dat', 'w') as file:
            file.write(pi)

    return(pi)

def piSearch(pi, ialist, verbose = True, positions = False):

    # setting variables
    if pi != str:
        str(pi)

    length = len(ialist)
    wrap = len(ialist[0])

    piplace = 0
    imglist = []
    piwrap = ""
    totaldigit = len(pi)
    palist = []

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

    if len(imglist) == 0 and verbose:
        print("There is no image in this variation of pi. But here is visualized pi anyways.")
        imglist.append(tpip)

    # constants and a print

    imglnum = 0
    piplace = 0
    if verbose:
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

    # This processes the 1s and 0s to the image and adds new lines
    for digit in pi:
        if digit == '0':
            vpi += "░"
        else:
            vpi += "█"
        if (piplace + 2) % wrap == 1:
            vpi += "\n"
        piplace += 1
        # And this here puts the START and END where the images start and end
        if piplace == imglist[imglnum] - wrap * length:
            vpi += starttext + '\n'
        if piplace == imglist[imglnum]:
            vpi += endtext + '\n'
            if len(imglist) - 1 > imglnum:
                imglnum += 1

    # Finally the print function, printing the already formatted visualized pi.
    if verbose:
        print(vpi)
    if positions:
        return(imglist)
    else:
        return(vpi)