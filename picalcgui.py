from main import piGen, piSearch
import PySimpleGUI as sg

# ialist = ['1001','0000'],'1001','0110']
ialist = ['0111', '1100', '1111', '0101']
wrap = len(ialist)


column1 = [
    [sg.Text('How many digits of pi?'),sg.InputText(size=(10))],
    [sg.Checkbox('Generate pi?',enable_events=True, key='initpigen')],
    [sg.Checkbox('Save pi?',enable_events=True, key='save')],
    [sg.Submit(key='submit')],
]
layout = [[sg.Column(column1,element_justification='center'), sg.VSep(pad=(5)), sg.MLine(key='vpigui'+sg.WRITE_ONLY_KEY, size=(wrap * 2,8))]]

window = sg.Window("piCalcGui", layout, margins=(10,10))

print = lambda *args, **kwargs: window['vpigui' + sg.WRITE_ONLY_KEY].print(*args, **kwargs)

initpigen = False
save = False

while not sg.WINDOW_CLOSED:
    DIGITS = 0
    while DIGITS < 2 or DIGITS == 1000:
        event = False
        while event != 'submit':
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                exit()
            if event == 'initpigen':
                initpigen = True
            if event == 'save':
                save = True
        DIGITS = values[0]
        DIGITS = int(DIGITS)

    pi = 3

    if initpigen:
        if save:
            pi = piGen(DIGITS, save=True)
            pi = pi[2:]
        else:
            pi = piGen(DIGITS)
            pi = pi[2:]

    else:
        # opens pi file and assigns it to pi
        DIGITS = str(DIGITS)
        with open(f'pi{DIGITS}.dat') as f:
            lpi = f.readlines()
        pi = lpi[0]
        pi = pi[2:]

    num = 1
    vpi = piSearch(pi,ialist, verbose=False)

    print(vpi)