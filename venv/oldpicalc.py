x = int(input("How many numbers of pi (the more numbers the more accurate)?: "))
ver = int(input("1 for Nilakantha Series (Nilakantha is recommended), 2 for Gregory-Leibniz: "))
def glb():
    neg = True
    global pi
    pi = 1
    num = 3
    for count in range(x):
        if neg == True:
            pi -= 1/num
            neg = False
        else:
            pi += 1/num
            neg = True
        num += 2
        if count % 10000 == 0:
            ppi = pi * 4
            print(ppi)
    pi *= 4
    print(pi)

def nlk():
    neg = False
    global pi
    pi = (3)
    num = 2
    for count in range(x):
        if neg == True:
            pi -= (4 / (num * (num+1) * (num+2)))
            neg = False
        else:
            pi += (4 / (num * (num + 1) * (num + 2)))
            neg = True
        num += 2
        if count % 10000 == 0:
            print(pi)


if ver == 1:
    glb()
if ver == 2:
    nlk()

print(pi)
