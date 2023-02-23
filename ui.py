import PySimpleGUI as sg

sg.theme("DarkAmber")

# Default crafting values
QTY = 10
DUR1 = 35
DUR2 = 9

inputs = [
    [
        sg.Text("Qty: "),
        sg.Push(),
        sg.Combo(
            values=list(range(100)),
            key="qty",
            size=(3, 1),
            enable_events=True,
            default_value=QTY,
            pad=(0, 10),
        ),
    ],
    [
        sg.Text("Macro 1 duration (s): "),
        sg.Push(),
        sg.Combo(
            values=list(range(40)),
            key="dur1",
            size=(3, 1),
            default_value=DUR1,
            pad=(0, 10),
        ),
    ],
    [
        sg.Text("Macro 2 duration (s): "),
        sg.Push(),
        sg.Combo(
            values=list(range(40)),
            key="dur2",
            size=(3, 1),
            default_value=DUR2,
            pad=(0, 10),
        ),
    ],
]

display_column = [
    [sg.Text("Crafted: "), sg.Text(size=(15, 1), key="crafted")],
]


layout = [
    [sg.Column(inputs), sg.VSeparator(), sg.Column(display_column)],
    [sg.HorizontalSeparator(pad=(0, 20))],
    [sg.Button("Craft"), sg.Button("Stop"), sg.Exit()],
]

window = sg.Window("Crafting Helper", layout, margins=(30, 30))
