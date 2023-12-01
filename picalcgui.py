from main import piGen, piSearch
import PySimpleGUI as sg

layout = [
    [sg.Text('How many digits of pi?'),sg.InputText()],
    [sg.Checkbox('Generate pi?',enable_events=True, key='initpigen')],
    [sg.Checkbox('Save pi?',enable_events=True, key='save')],
    [sg.Submit(key='submit')]
]

window = sg.Window("Demo", layout, margins=(100,100))

initpigen = False
save = False

while True:
    event, values = window.read()
    if event == 'initpigen':
        initpigen = True
    if event == 'initpigen' and event == 'save':
        save = True
    DIGITS = values[0]
    DIGITS = int(DIGITS)
    if event == 'submit':
        break

pi = 3

if initpigen == True:
    pi = piGen(DIGITS)
    pi = pi[2:]

else:
    # opens pi file and assigns it to pi
    DIGITS = str(DIGITS)
    with open(f'pi{DIGITS}.dat') as f:
        lpi = f.readlines()
    pi = lpi[0]
    pi = pi[2:]

# ialist = ['1001','0000'],'1001','0110']
ialist = ['0111', '1100', '1111', '0101']
vpi = piSearch(pi,ialist)

layout = [sg.Multiline(key='vpi')]