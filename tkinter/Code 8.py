from tk_scene import scene
from tkinter import *

sceneLayout = (
    (())
)

w = Tk()

def day():
    global Sun
    global Moon
    Sun = True
    Moon = False
    return True

l1 = Label(w, text="Is it Day or Night"\
                         "real? (Enter \"day\" or \"night\")")
buttonDay = Button(w, text='Day', command=day)

w.mainloop()
