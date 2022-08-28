import os
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
import time, sqlite3


class App():
    def __init__(self):
        #Sqlite3
        self.conn = sqlite3.connect('usuarios.db') # Conexão Database
        self.c = self.conn.cursor() # Cursor DB
        self.data()
        self.configWin()
        self.widgets()
        self.win.mainloop()

    def data(self):
        self.dia = time.strftime("%d/%m/%y") # Obtendo Data atual

    def hr(self):
        self.hora = time.strftime("%H:%M") # Obtendo horario atual 

    def configWin(self):
        self.win = Tk()
        self.win.title('TecnoBreve - HORA X HORA')
        self.win.geometry("800x500+100+100")
        self.win.iconbitmap(r'icon.ico')
        self.win.resizable(width=False, height=False)

    def widgets(self):
        # Abreviando win - Opcional------------------------------------
        win = self.win

        # Imagens------------------------------------------------------
        self.mainFrameImg = PhotoImage(file="img//mainFrame.png")
        self.frameLoginImg = PhotoImage(file="img//frameLogin.png")
        self.frameCadImg = PhotoImage(file="img//frameCad.png")

        # Frames------------------------------------------------------
        fmL = self.frameLogin = Frame(win)
        fmM = self.mainFrame = Frame(win)
        fmC = self.frameCad = Frame(win)

        # Labels BG's--------------------------------------------------
        self.lblFundo = Label(fmL, image=self.frameLoginImg)
        self.lblFundo2 = Label(fmC, image=self.frameCadImg)
        self.lblFundo3 = Label(fmM, image=self.mainFrameImg)


        # Buttons------------------------------------------------------
        self.btn = Button(fmL, text = 'Logar', font = 'OpenSans 16', bg  = "Black", fg = 'White', width = 47, command= self.login)
        self.btnCad = Button(fmL, text = 'Novo Usuário', font = 'OpenSans 16', bg  = "Grey", fg = 'Black', width = 47, command = self.newUser)
        
        # Cadastro
        self.btnSalvar = Button(fmC, text = 'SALVAR!', font = 'OpenSans 16', bg  = "Black", fg = 'white', width = 47)

        # Texts and Entrys---------------------------------------------
        self.user = Entry(fmL, width = 26, font = 'OpenSans 16', borderwidth = 0)
        self.senha = Entry(fmL, width = 26, font = 'OpenSans 16', borderwidth = 0, show = '*')

        # Cadastro
        self.nomeCad = Entry(fmC, width = 26, font = 'OpenSans 16', borderwidth = 0)
        self.matriculaCad = Entry(fmC, width = 26, font = 'OpenSans 16', borderwidth = 0)
        self.emailCad = Entry(fmC, width = 26, font = 'OpenSans 16', borderwidth = 0)
        self.senhaCad = Entry(fmC, width = 26, font = 'OpenSans 16', borderwidth = 0)
        self.senharCad = Entry(fmC, width = 26, font = 'OpenSans 16', borderwidth = 0)

        # Main
        self.texto = Text(fmM, height=5, width=40, borderwidth=4)
        self.mainData = Label(fmM, text=f"Data: {self.dia}", fg = 'Black', bg = 'White', font = 'Arial 12 bold')
        self.btnH = Button(fmM, text = 'Fazer Hora X Hora', bg = 'Black', fg = 'White',font='Arial 18 bold',width=20, height=1, command=self.parcial)

        # Instanciar---------------------------------------------------
        self.instaciar()
        
    def instaciar(self):
        # Widgets
        # Login
        self.user.place(x= 270, y=135)
        self.senha.place(x= 230, y= 235)
        self.btn.place(x=115, y=320)
        self.btnCad.place(x=115, y=370)

        # Cad
        self.nomeCad.place(x = 230, y = 110)
        self.matriculaCad.place(x = 260, y = 165)
        self.emailCad.place(x = 230, y = 220)
        self.senhaCad.place(x = 230, y = 275)
        self.senharCad.place(x = 230, y = 330)
        self.btnSalvar.place(x = 100, y = 400)

        # Main
        self.texto.place(x=0, y = 200)
        self.mainData.place(x=600, y=20)
        self.btnH.place(x=516, y=100)

        # Background!
        self.lblFundo.pack()

        # Frame
        self.frameLogin.pack()
    
    # Funcções
    def newUser(self):
        self.frameLogin.destroy()
        self.lblFundo2.pack()
        self.frameCad.pack()

    def login(self):
        self.frameLogin.destroy()
        self.lblFundo3.pack()
        self.mainFrame.pack()

    def parcial(self):
        stxt = self.texto.get('1.0', END)
        self.msgb(1,'Inciando! Aguarde')
        if stxt != '':
            arquivo = open('texto.txt', 'w')
            arquivo.write(stxt)
            arquivo.close()
            import back
            self.msgb(1, 'Right!!')
        else:
            self.msgb(2, 'Coloque as credenciais !')
    def msgb(self, tp, msg):
        if tp == 1:
            messagebox.showinfo('TECNOBREVE ₢', msg)
        elif tp == 2:
            messagebox.showerror('TECNOBREVE ₢', msg)

App()
