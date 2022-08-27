from tkinter import *
from tkinter import messagebox
import os,sys, time
import sqlite3 as sq

conn = sq.connect('usuarios.db')
c = conn.cursor()

win = Tk()
win.title('HORA X HORA')
win.geometry('800x500+0+0')
win.resizable(width = False, height = False)

def troca():
    matricula = user.get()
    pas = senha.get()

    if matricula == '4054752' and pas == '8458':
        lbl_fundo['image'] = main_image
        btn.destroy()
        user.destroy()
        senha.destroy()
        btnCad.destroy()
    else:
        messagebox.showerror('Login Inválido', 'Insira um login correto!')

def newCad():
    lbl_fundo['image'] = cad_image
    btn.destroy()
    user.destroy()
    senha.destroy()
    btnCad.destroy()

login_image = PhotoImage(file="img/frameLogin.png")
cad_image = PhotoImage(file="img/frameCad.png")
main_image = PhotoImage(file="img/mainFrame.png")

lbl_fundo = Label(win, image = login_image)

user = Entry(win, width = 26, font = 'OpenSans 16', borderwidth = 0)
senha = Entry(win, width = 26, font = 'OpenSans 16', borderwidth = 0, show = '*')
btn = Button(win, text = 'Logar', font = 'OpenSans 16', bg  = "Black", fg = 'White', width = 47, command = troca)
btnCad = Button(win, text = 'Novo Usuário', font = 'OpenSans 16', bg  = "Grey", fg = 'Black', width = 47, command = newCad)

lbl_fundo.pack()

user.place(x= 270, y=135)
senha.place(x= 230, y= 235)
btn.place(x=115, y=320)
btnCad.place(x=115, y=370)

win.mainloop()
