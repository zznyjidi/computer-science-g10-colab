from tk_scene import scene
from tkinter import *
import random

sceneLayout = (
    (("prompt", "label", {"text": "(Press Button Below to Start)"}),),
    (("continue", "button", {"text": "Start"}),)
)

def createScene(sceneIndex):
    global window
    window = scene(sceneLayout[sceneIndex])

window = None
createScene(0)
window.startWindow()

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

islife = None
def time():
    global islife
    global w2
    w2 = Toplevel()
    if daytime:
        l2 = Label(w2, text="Put the 3 most common clouds in order from smallest"\
              "to largest: Stratocumulus, Cumulus, Cumulonimbus: ")
        e1, e2, e3 = Entry(w2), Entry(w2), Entry(w2)
        if e1.get() == 'Stratocumulus' and e2.get() == 'Cumulus' and e3.get() == 'Cumulonimbus':
            l3 = Label(w2, text='Correct, advance to the next round')
            islife = True
        else:
            l3 = Label(w2, text='Incorrect (Why did you not search online?)')
            iflife = False
    else:
        l2 = Label(w2, text="What is the thunder cloud Pokemon? ")
        e1 = Entry(w2)
        if e1.get() == 'thundurus':
            l3 = Label(w2, text='Correct (you probably searched online)')
            islife = True
        else:
            l3 = Label(w2, text='Incorrect (Why did you not search online?)')
            islife = False

instruction = Label(w, text='''Welcome User428, this is the CIA's secret"\
    operation. Operation SKYFALL.
    During 1898, we have replaced birds with drones,"\
    and now in the past 5 years we have"\
    been working on deleting the sky ")
    Lets see how loyal you are to our cause…''')

l1 = Label(w, text="Is it Day or Night"\
                         "real? (Enter \"day\" or \"night\")")
buttonDay = Button(w, text='Day', command=day)

def mathq():
    equations = [
        ("54 * 3", 54 * 3),
        ("847 / 11", 847 / 11),
        ("21 * 12", 21 * 12),
        ("5 * 10 + 35", 5 * 10 + 35),
        ("9898 / 98", 9898 / 98)
    ]
    equation, correct_answer = random.choice(equations)
    l5 = Label(w3, text=equation)
    e4 = Entry(w3)
    if e4.get() == correct_answer:
        return
    else:
        l6 = Label(w3, text='Wrong answer')
        w.destroy()
        w2.destroy()
        w3.destroy()

def true_ending():
    l7 = Label(w2, text="Welcome User428. To further understand why"\
              "the sky and the Sun are not real, we must go")
    l8 = Label(w2, text="back to 2021 when COVID started. Truth be told,"\
          "COVID was a lie created")
    l9 = Label(w2, text="as a joint operation with China and America to remove the sky.")
    l10 = Label(w2, text="Now they have set their sights on revealing to"\
          "the world that we live in")
    l11 = Label(w2, text="the matrix. Your mission, should you choose to"\
          "accept, is to save the world.")
    w.destroy()
    w2.destroy()
    w3.destroy()
    

def ending():
    global w3
    w3 = Toplevel()
    l4 = Label(w3, text='So I see you’ve come to the end of the program."\
          "To ensure you are a real person, please enter the"\
          "code given to you after you complete a question.')
    mathq()
    if islife:
        code = Label(w2, text='Correct! Your code is 80.932')
    else:
        l6 = Label(w2, text='Wrong answer')
        w.destroy()
        w2.destroy()
        w3.destroy()
    ecode = Entry(w2)
    if ecode.get() == 80.932:
        true_ending()
    else:
        w.destroy()
        w2.destroy()
        w3.destroy()



w.mainloop()
