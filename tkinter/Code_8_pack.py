from tkinter import *
import random

w = Tk()
w.title('Code 8')

daytime = None

def day():
    global Sun
    global Moon
    global daytime
    Sun = True
    Moon = False
    daytime = True
    time()

def night():
    global Sun
    global Moon
    global daytime
    Sun = False
    Moon = True
    daytime = False
    time()

islife = None

def sbmt1():
    global islife
    if e1.get() == 'Stratocumulus' and e2.get() == 'Cumulus' and e3.get() == 'Cumulonimbus':
            l3 = Label(w2, text='Correct, advance to the next round')
            l3.pack()
            islife = True
            ending()
    else:
            l3 = Label(w2, text='Incorrect (Why did you not search online?)')
            l3.pack()
            islife = False
    

def sbmt2():
    global islife
    if e1.get() == 'thundurus':
            l3 = Label(w2, text='Correct (you probably searched online)')
            l3.pack()
            islife = True
            ending()
    else:
            l3 = Label(w2, text='Incorrect (Why did you not search online?)')
            l3.pack()
            islife = False
    

def sbmt3():
    global ecode
    if float(ecode.get()) == 80.932:
        true_ending()
    else:
        exit()


def sbmt4():
    global ecode
    if float(e4.get()) == correct_answer:
        if islife:
            code = Label(w3, text='Correct! Your code is 80.932')
            code.pack()
        else:
            l6 = Label(w3, text='Wrong answer')
            l6.pack()
            exit()
        elabel = Label(w3, text='Code: ')
        elabel.pack()
        ecode = Entry(w3)
        ecode.pack()
        submit3 = Button(w3, text='Submit', command=sbmt3)
        submit3.pack()
    else:
        l6 = Label(w3, text=f"Sorry, the correct answer is {correct_answer}.")
        l6.pack()
        exit()


def time():
    global islife
    global w2
    global e1, e2, e3
    w2 = Tk()
    if daytime:
        l2 = Label(w2, text="Put the 3 most common clouds in order from smallest"\
              "to largest: Stratocumulus, Cumulus, Cumulonimbus: ")
        l2.pack()
        e1, e2, e3 = Entry(w2), Entry(w2), Entry(w2)
        e1.pack()
        e2.pack()
        e3.pack()
        submit1 = Button(w2, text='Submit', command=sbmt1)
        submit1.pack()
        
    else:
        l2 = Label(w2, text="What is the thunder cloud Pokemon? ")
        l2.pack()
        e1 = Entry(w2)
        e1.pack()
        submit2 = Button(w2, text='Submit', command=sbmt2)
        submit2.pack()
        
def ending():
    global w3, ecode
    w3 = Tk()
    l4 = Label(w3, text='So I see you’ve come to the end of the program.\n\
          To ensure you are a real person, please enter the code given to you after you complete a question.')
    l4.pack()
    mathq()
    
    

def mathq():
    global e4, correct_answer
    equations = [
        ("54 * 3", 54 * 3),
        ("847 / 11", 847 / 11),
        ("21 * 12", 21 * 12),
        ("5 * 10 + 35", 5 * 10 + 35),
        ("9898 / 98", 9898 / 98)
    ]
    equation, correct_answer = random.choice(equations)
    l5 = Label(w3, text=equation)
    l5.pack()
    e4 = Entry(w3)
    e4.pack()
    submit4 = Button(w3, text='Submit', command=sbmt4)
    submit4.pack()

def Quit():
    exit()

def true_ending():
    w4 = Toplevel()
    l7 = Label(w4, text="Welcome User428. To further understand why"\
              "the sky and the Sun are not real, we must go")
    l8 = Label(w4, text="back to 2021 when COVID started. Truth be told,"\
          "COVID was a lie created")
    l9 = Label(w4, text="as a joint operation with China and America to remove the sky.")
    l10 = Label(w4, text="Now they have set their sights on revealing to"\
          "the world that we live in")
    l11 = Label(w4, text="the matrix. Your mission, should you choose to"\
          "accept, is to save the world.")
    l7.pack()
    l8.pack()
    l9.pack()
    l10.pack()
    l11.pack()
    quitbutton = Button(w4, text='Quit', command=Quit)
    quitbutton.pack()


instruction = Label(w, text='''Welcome User428, this is the CIA's secret operation. Operation SKYFALL.\n
    During 1898, we have replaced birds with drones, and now in the past 5 years we have 
been working on deleting the sky
Lets see how loyal you are to our cause…''')
instruction.pack()

l1 = Label(w, text="Is it Day or Night"\
                         "real? (Enter \"day\" or \"night\")")
l1.pack()
buttonDay = Button(w, text='Day', command=day)
buttonNight = Button(w, text='Night', command=night)
buttonDay.pack()
buttonNight.pack()

w.mainloop()
