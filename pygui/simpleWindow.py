

import PySimpleGUI as sg
 


# sg.Popup('Mi primera ventanita', button_color=('black', 'red'))
# sg.PopupYesNo('Mi primera ventanita', button_color=('black', 'green'))

# sg.PopupOKCancel('Mi primera ventanita', button_color=('black', 'grey'))
# texto = sg.PopupGetText('Titulo', 'Ingresá algo')
# sg.Popup('Resultados', 'Ingresaste el siguiente texto: ', texto)

# sg.Window(title="Hola Mundo!", layout=[[]], margins=(200  , 200)).read()

layout = [[sg.Text("Hola Mundo!")], [sg.Button("OK")]]
window = sg.Window("Primera Demo", layout, margins=(200, 150))
while True:
  event, values = window.read()
  if event == "OK" or event == sg.WIN_CLOSED:
    break
window.close()