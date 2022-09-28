import eel

eel.init("web")

@eel.expose
def new_window(target: str):
    eel.show(f"html/{target}")

eel.start("index.html", size=(700, 700))
eel.show("main.html", size=(700, 700))
eel.show("learn.html", size=(700, 700))
eel.show("test.html", size=(700, 700))
