import FreeSimpleGUI as sg

sg.theme('DarkAmber')

layout = [
    [sg.Text('¡Hola, mundo con FreeSimpleGUI!')],
    [sg.InputText(key='-INPUT-')],
    [sg.Button('Aceptar'), sg.Button('Salir')]
]

window = sg.Window('Ventana Básica', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Salir':
        break
    print('Entrada:', values['-INPUT-'])

window.close()