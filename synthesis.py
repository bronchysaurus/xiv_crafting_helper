from pywinauto.application import Application
import time

import ui


APP = "FINAL FANTASY XIV"
# default keypresses for macros 1 and 2
DEFAULT_MACRO1 = "1"
DEFAULT_MACRO2 = "2"

app = Application(backend="win32").connect(title_re=f"{APP}", visible_only=True)
window = app.top_window()
stop = False  # stops the crafting loop

def select_synthesis():
    for _ in range(5):
        window.send_keystrokes("{VK_NUMPAD0}")
        time.sleep(0.05)

    time.sleep(2.5) # wait for synthesis window to appear


# start synthesis
def start(values):
    crafted = 0
    qty = int(values["qty"] or 0)
    dur1 = int(values["dur1"] or 0)
    dur2 = int(values["dur2"] or 0)

    ui.window["crafted"].update(value=f"{crafted}/{qty}")

    for _ in range(qty):
        if stop:
            break

        select_synthesis()

        # Macro 1
        if dur1 > 0:
            window.send_keystrokes(DEFAULT_MACRO1)
            time.sleep(dur1 + 1) # wait an extra second to account for lag

        # Macro 2
        if dur2 > 0:
            window.send_keystrokes(DEFAULT_MACRO2)
            time.sleep(dur2 + 1) # wait an extra second to account for lag

        crafted += 1
        ui.window["crafted"].update(value=f"{crafted}/{qty}")
        ui.window.refresh()

        # wait for crafting window to appear
        time.sleep(2)
