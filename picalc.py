import time

# Linux
# import sys
# sys.set_int_max_str_digits(999999999)

def piGen(DIGITS,save = False):

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
                if goes % 1000 == 0:
                    ips = time.time() - st
                    totaltime = totaltime + ips
                    st = time.time()
                    if goes == 1000:
                        ips = 1000 / ips
                        tbf = ips / (x / 1000)
                        tbf = x / tbf
                        tbf *= 1.05
                        tbf += tbf * 0.05
                        print(f"Estimated {tbf:.2f} seconds till finish.\n")
                    print(f"Elapsed time: {totaltime:.2f} out of {tbf:.2f}")
                    print(f"Percentage finished: {goes / DIGITS * 100:.2f}%\n")

        print("True time to finish:", time.time() - it)

    digits = [str(n) for n in list(pi_digits(DIGITS))]
    pi = ("%s.%s\n" % (digits.pop(0), "".join(digits)))

    pi = pi[2:]
    pi = int(pi)
    pi = bin(pi)

    if save:
        with open(f'pi{DIGITS}.dat', 'w') as file:
            file.write(pi)

    return(pi)