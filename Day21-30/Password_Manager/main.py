# Day 29 - Password Manager

from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, END
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json
PATH = 'Day21-30/Password_Manager/'


# ---------------------------- PASSWORD GENERATOR -------------------------- #
def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = letter_list + number_list + symbol_list

    shuffle(password_list)

    password = ''.join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pyperclip.copy(pass_entry.get())

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = site_entry.get()
    user = user_entry.get()
    password = pass_entry.get()

    new_data = {
        website: {
            'username': user,
            'password': password,
        }
    }

    if len(site_entry.get()) == 0 or len(user_entry.get()) == 0 \
            or len(pass_entry.get()) == 0:
        messagebox.showerror(
            title='You done goofed',
            message="Please don't leave any fields empty."
        )
        return
    else:
        try:
            with open(PATH+'data.json', mode='r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(PATH+'data.json', mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open(PATH+'data.json', mode='w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            site_entry.delete(0, END)
            pass_entry.delete(0, END)


# ------------------------PASSWORD RETRIEVAL--------------------------- #

def find_password():
    website = site_entry.get()

    try:
        with open(PATH+'data.json') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(
            title='Error',
            message='No Data File Found.'
        )
    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website,
                message=f'Username: {username}\n'
                f'Password: {password}'
            )
        else:
            messagebox.showerror(
                title='Error',
                message=f'No details for {website} exists.'
            )


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(
    padx=20,
    pady=20
)

canvas = Canvas(
    width=200,
    height=200
)
lock_image = PhotoImage(file='Day21-30/Password_Manager/logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

site_label = Label(
    text='Website:'
)
site_label.grid(row=1, column=0)

site_entry = Entry(
    width=33
)
site_entry.focus()
site_entry.grid(row=1, column=1)

search_button = Button(
    text='Search',
    width=15,
    command=find_password
)
search_button.grid(row=1, column=2)

user_label = Label(
    text='Email/Username:'
)
user_label.grid(row=2, column=0)

user_entry = Entry(
    width=52
)
user_entry.insert(0, 'chriskusha@yahoo.com')
user_entry.grid(row=2, column=1, columnspan=2)

pass_label = Label(
    text='Password:'
)
pass_label.grid(row=3, column=0)

pass_entry = Entry(
    width=33
)
pass_entry.grid(row=3, column=1)

generator_button = Button(
    text='Generate Password',
    command=generate_password
)
generator_button.grid(row=3, column=2)

add_button = Button(
    text='Add',
    width=44,
    command=save
)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
