import PySimpleGUI as sg


def Calc_MW(a, b):
    if a > b:
        first = a
        second = b
    else:
        first = b
        second = a
    z1 = round((second - 1.0073) / (first - second))
    z2 = z1 + 1
    z3 = z1 + 2
    z0 = z1 - 1
    M1 = z1 * first - z1 * 1.0073
    M2 = z2 * second - z2 * 1.0073
    M = round((M1 + M2) / 2, 4)
    zero = round((M + z0 * 1.0073) / z0, 4)
    third = round((M + z3 * 1.0073) / z3, 4)
    return zero, third, M


def GUI():
    sg.theme('GrayGrayGray')
    frame = [
        [sg.Text('检验前一个峰的m/z='), sg.Text(size=(8, 1), key='-FIRSTPEAK-')],
        [sg.Text('检验后一个峰的m/z='), sg.Text(size=(8, 1), key='-SECONDPEAK-')],
        [sg.Text('分子量(Da)='), sg.Text(size=(10, 1), key='-RESULT-')]
    ]
    # 界面布局
    layout = [[sg.Text('请输入两个相邻簇峰的m/z')],
              [sg.Text('第一个m/z='), sg.InputText(size=10)],
              [sg.Text('第二个m/z='), sg.InputText(size=10)],
              [sg.Button('Exit', size=8), sg.Button('计算', size=8)],
              [sg.Frame('计算结果', frame, title_color='red')]
    ]
    # 创造窗口
    window = sg.Window('分子量计算器', layout, size=(260, 230))
    # 事件循环并获取输入值
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        a = float(values[0])
        b = float(values[1])
        c = Calc_MW(a, b)
        window['-FIRSTPEAK-'].update(c[1])
        window['-SECONDPEAK-'].update(c[0])
        window['-RESULT-'].update(c[2])


if __name__ == '__main__':
    try:
        GUI()
    except Exception as e:
        sg.popup_error(f'运行出错!\n报错信息：', e)
