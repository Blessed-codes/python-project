# This program convert a value from fahrenhrit to celsisus
from tkinter import *

def fah_to_celcius():
    fahrenheit = int(fah_value.get())
    celcius_value = ((fahrenheit - 32) * (5 / 9))
    cel_value.config(text=round(celcius_value, 2))

window = Tk()
window.config(padx=50, pady=50)

window.title(" Temperature Converter")

fah_label = Label(text="Fahrenheit", font=("Ariel", 20, "bold"), padx=20)
fah_label.grid(column=3, row=1, pady=20)

fah_value = Entry(width=10, font=("Ariel", 20, "bold"))
fah_value.grid(column=1, row=1)

cel = Label(text="Celcius", font=("Ariel", 20, "bold"))
cel.grid(column=3, row=4)

cel_value = Label(text=0, font=("Ariel", 20, "bold"))
cel_value.grid(column=1, row=4, pady=20)

calculate = Button(text="convert", command=fah_to_celcius)
calculate.grid(column=2, row=6)


window.mainloop()