from threading import Thread

from ui import window, sg
import synthesis


while True:  # Event Loop
    event, values = window.read()  # type: ignore
    if event == sg.WIN_CLOSED or event == "Exit":
        break

    synthesis.stop = False

    if event == "Stop":
        synthesis.stop = True

    if event == "Craft":
        t = Thread(target=synthesis.start, args=(values,), daemon=True).start()

window.close()
