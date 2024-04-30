import tkinter as tk

elementList = {
    "label": tk.Label,
    "button": tk.Button,
    "entry": tk.Entry,
    "frame": tk.Frame, 
    "checkbutton": tk.Checkbutton,
    "radiobutton": tk.Radiobutton
}

class element:
    element = None
    propertys = {}
    packPropertys = ""

    def __init__(this, parentObject, element):
        this.element = element(parentObject)

    def addArgs(this, args):
        for arg, key in args.items():
            this.propertys[arg] = key   
            if type(key) in [str]: 
                exec(f"this.element.config({arg}=\"{key}\")")
            elif arg == "command" and str(type(key)) in "<class 'function'>":
                this.element.config(command=key)
            else:
                exec(f"this.element.config({arg}={key})")

    def addPackArgs(this, args):
        for arg, key in args.items():
            if type(key) in [int,float,bool]:
                this.packPropertys += f"{arg}={key}, "
            else:
                this.packPropertys += f"{arg}=\"{key}\", "
        this.packPropertys = this.packPropertys[:len(this.packPropertys)-2]

    def pack(this):
        exec(f"this.element.pack({this.packPropertys})")

class scene:
    window = None
    elements = {}

    def __init__(this, layout=None):
        this.window = tk.Tk()
        for row in range(len(layout)):
            this.elements[f"_frameRow{row}"] = element(this.window, elementList["frame"])
            this.elements[f"_frameRow{row}"].addPackArgs({"fill": "both","expand": True})
            this.elements[f"_frameRow{row}"].pack()
            for elementIndex in range(len(layout[row])):
                thisElement = layout[row][elementIndex]
                this.elements[thisElement[0]] = element(this.elements[f"_frameRow{row}"].element, elementList[thisElement[1]])
                this.elements[thisElement[0]].addArgs(thisElement[2])
                this.elements[thisElement[0]].addPackArgs({"side": "left"})
                this.elements[thisElement[0]].pack()

    def startWindow(this):
        this.window.mainloop()

    def setGeometry(this, height, width):    
        this.window.geometry(f"{height}x{width}")
