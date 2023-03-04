# Day 27 - Mile to Km Converter GUI

from tkinter import Tk, Label, Button, Entry


def mile_to_km():
    km = float(miles.get()) * 1.60934
    kilometers['text'] = f'{km}'


window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)

miles = Entry(width=7)
miles.grid(row=0, column=1)

mile_label = Label(text='Miles')
mile_label.grid(row=0, column=2)

is_equal_label = Label(text='is equal to')
is_equal_label.grid(row=1, column=0)

kilometers = Label(text='0')
kilometers.grid(row=1, column=1)

km_label = Label(text='Km')
km_label.grid(row=1, column=2)

calc_button = Button(
    text='Calculate',
    command=mile_to_km
)
calc_button.grid(row=2, column=1)

window.mainloop()
