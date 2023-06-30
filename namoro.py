import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox


root = tk.Tk()
root.title('')
root.geometry('500x500')
root.configure(background='#ffc8dd')


def butao_de_mover(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 50:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)


def aceitou():
    messagebox.showinfo(
        '', 'Agora vamos jogar um Red Dead Redemption 2')


def negou():
    button_1.destroy()


margin = Canvas(root, width=500, bg='#ffc8dd', height=100,
                bd=0, highlightthickness=0, relief='ridge')
margin.pack()
text_id = Label(root, bg='#ffc8dd', text='Quer namorar comigo?',
                fg='#590d22', font=('Montserrat', 24, 'bold'))
text_id.pack()
button_1 = tk.Button(root, text='Não', bg='#ffb3c1', command=negou,
                     relief=RIDGE, bd=3, font=('Montserrat', 8, 'bold'))
button_1.pack()
root.bind('<Motion>', butao_de_mover)
button_2 = tk.Button(root, text='Sim', bg='#ffb3c1', relief=RIDGE,
                     bd=3, command=aceitou, font=('Montserrat', 14, 'bold'))
button_2.pack()


root.mainloop()