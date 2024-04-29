from tk_scene import scene
from tkinter import *

sceneLayout = (
    (())
)

w = Tk()

daytime = None

def day():
    global Sun
    global Moon
    Sun = True
    Moon = False
    daytime = True
    time()

def night():
    global Sun
    global Moon
    Sun = False
    Moon = True
    daytime = False
    time()
    
def time():
    w2 = Toplevel()
    if daytime:
        l2 = Label(w2, text="Put the 3 most common clouds in order from smallest"\
              "to largest: Stratocumulus, Cumulus, Cumulonimbus: ")
        e1, e2, e3 = Entry(w2), Entry(w2), Entry(w2)
        if e1.get() == 'Stratocumulus' and e2.get() == 'Cumulus' and e3.get() == 'Cumulonimbus':
            l3 = Label(w2, text='Correct, advance to the next round')
        else:
            l3 = Label(w2, text='Incorrect (Why did you not search online?)')
    else:
        l2 = Label(w2, text="What is the thunder cloud Pokemon? ")
        e1 = Entry(w2)
        if e1.get() == 'thundurus':
            l3 = Label(w2, text='Correct (you probably searched online)')
        else:
            l3 = Label(w2, text='Incorrect (Why did you not search online?)')

instruction = Label(w, text='''Welcome User428, this is the CIA's secret"\
    operation. Operation SKYFALL.
    During 1898, we have replaced birds with drones,"\
    and now in the past 5 years we have"\
    been working on deleting the sky ")
    Lets see how loyal you are to our cause…''')

l1 = Label(w, text="Is it Day or Night"\
                         "real? (Enter \"day\" or \"night\")")
buttonDay = Button(w, text='Day', command=day)



w.mainloop()
