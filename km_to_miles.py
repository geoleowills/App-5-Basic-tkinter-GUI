from tkinter import *

window = Tk()


def km_to_miles():
    grams = float(e1_value.get())*1000
    tgrams.delete("1.0", END)
    tgrams.insert(END, grams)
    pounds = float(e1_value.get())*2.20462
    tpounds.delete("1.0", END)
    tpounds.insert(END, pounds)
    ounces = float(e1_value.get())*35.274
    tpounds.delete("1.0", END)
    tounces.insert(END, ounces)


b1 = Button(window, text="Convert", command=km_to_miles)
b1.grid(row=0, column=2)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=0)
t1.insert(INSERT, "Kg")


tgrams = Text(window, height=1, width=20)
tgrams.grid(row=1, column=0)

tpounds = Text(window, height=1, width=20)
tpounds.grid(row=1, column=1)

tounces = Text(window, height=1, width=20)
tounces.grid(row=1, column=2)


window.mainloop()
