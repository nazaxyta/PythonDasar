import PySimpleGUI as sg
import datetime

def main():
    hours = [f'{i:02d}' for i in range(24)]
    minutes = [f'{i:02d}' for i in range(60)]
    layout = [
        [sg.Text('Nomor Polisi'), sg.Input(key='-PLATENUMBER-')],
        [sg.Text('Waktu Masuk'), sg.Combo(hours, key='-ENTRYHOUR-'), sg.Text(':'), sg.Combo(minutes, key='-ENTRYMINUTE-')],
        [sg.Text('Waktu Keluar'), sg.Combo(hours, key='-EXITHOUR-'), sg.Text(':'), sg.Combo(minutes, key='-EXITMINUTE-')],
        [sg.Button('Hitung Biaya Parkir')],
        [sg.Text('Biaya Parkir'), sg.Text('', key='-PARKINGFEE-')]
    ]

    window = sg.Window('Program Parkir', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Hitung Biaya Parkir':
            entry_time = datetime.datetime.strptime(f'{values["-ENTRYHOUR-"]}:{values["-ENTRYMINUTE-"]}', '%H:%M')
            exit_time = datetime.datetime.strptime(f'{values["-EXITHOUR-"]}:{values["-EXITMINUTE-"]}', '%H:%M')
            parking_fee = (exit_time - entry_time).total_seconds() / 3600 * 2000
            window['-PARKINGFEE-'].update(f'{parking_fee:.2f}')
            sg.popup(f'Biaya parkir: {parking_fee:.2f}')

    window.close()

if __name__== '__main__':
    main()