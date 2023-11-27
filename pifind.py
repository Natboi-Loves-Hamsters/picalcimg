from picalc import piGen, piSearch

finaldig = int(input("What digit do you want pi searched till?: "))
save = True
dig = 2
ialist = ['0111', '1100', '1111', '0101']
if save:
    with open(f'pifull{finaldig}.dat', 'w', encoding="utf-8") as file:
        file.write('')

while finaldig > dig:
    pi = piGen(dig, False, False)
    pi = pi[2:]
    vpi = (piSearch(pi, ialist, False))
    if save:
        with open(f'pifull{finaldig}.dat', 'a', encoding="utf-8") as file:
            file.write(vpi)
            file.write(f'\n\ndig: {dig}\n')
    dig += 1
    if dig == 1000 and finaldig != 1000:
        dig += 1