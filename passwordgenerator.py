from tkinter import *
import random, string
import pyperclip

root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("Email - PASSWORD GENERATOR")

pass_string = StringVar()


def Generator():
    password = ''
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password + random.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_string.set(password)


heading = Label(root, text='PASSWORD GENERATOR', font='arial 15 bold').pack()
heading2 = Label(root, text='\nPassword Length', font='arial 13 ').pack()
pass_len = IntVar()
sp = Spinbox(root, from_=8, to=15, textvariable=pass_len).pack()

Button(root, text="GENERATE PASSWORD", command=Generator).pack(pady=5)
Entry(root, textvariable=pass_string).pack()


def copy_password():
    pyperclip.copy(pass_string.get())


Button(root, text='COPY TO CLIPBOARD', command=copy_password).pack(pady=5)
root.mainloop()
