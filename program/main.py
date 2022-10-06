from tkinter import *
from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Entry, Style
import tkinter as ttk
import tkinter as os

class MyApp(Tk):
    def __init__(self):
        Tk.__init__(self) 
        # Основное приложение
        window = ttk.Frame(self)
        window.pack()
        self.frames = {}
        for F in (PageOne, PageTwo, PageThree, PageFour):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='NSEW')
        self.show_frame(PageOne)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class PageOne(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.make_widget()

    def open_file():
        os.system()

    def make_widget(self):
        Style().configure("TButton", padding=(0, 20, 0, 20), font='serif 10')

        self.cvs = Canvas(self, height="1050", width="1680", background="#7F7FD5")

        # demo button to change page
        btnChange1 = Button(self.cvs, text="1", width=200, command=lambda: self.controller.show_frame(PageTwo))
        btnChange1 .grid(row=1, column=6, pady = 10)
        btnChange2 = Button(self.cvs, text="2", width=200, command=lambda: self.controller.show_frame(PageTwo))
        btnChange2 .grid(row=2, column=6, pady = 10)
        btnChange3 = Button(self.cvs, text="3", width=200, command=lambda: self.controller.show_frame(PageTwo))
        btnChange3 .grid(row=3, column=6, pady = 10)
        btnChange4 = Button(self.cvs, text="4", width=200, command=lambda: self.controller.show_frame(PageTwo))
        btnChange4 .grid(row=4, column=6, pady = 10)
        btnChange5 = Button(self.cvs, text="5", width=200, command=lambda: self.controller.show_frame(PageTwo),)
        btnChange5 .grid(row=5, column=6, pady = 10)
        btnChange6 = Button(self.cvs, text="6", width=200, command=lambda: self.controller.show_frame(PageTwo),)
        btnChange6 .grid(row=6, column=6, pady = 10)
        btnChange7 = Button(self.cvs, text="7", width=200, command=lambda: self.controller.show_frame(PageTwo),)
        btnChange7 .grid(row=7, column=6, pady = 10)
        btnChange8 = Button(self.cvs, text="8", width=200, command=lambda: self.controller.show_frame(PageTwo),)
        btnChange8 .grid(row=8, column=6, pady = 10)
        btnChange9 = Button(self.cvs, text="9", width=200, command=lambda: self.controller.show_frame(PageTwo),)
        btnChange9 .grid(row=9, column=6, pady = 10)
        btnChange10 = Button(self.cvs, text="10", width=200, command=lambda: self.controller.show_frame(PageTwo),)
        btnChange10 .grid(row=10, column=6, pady = 10)
        btnChange11 = Button(self.cvs, text="11", width=200, command=lambda: self.controller.show_frame(PageTwo),)
        btnChange11 .grid(row=11, column=6, pady = 10)
        btnChange12 = Button(self.cvs, text="12", width=200, command=lambda: self.controller.show_frame(PageTwo),)
        btnChange12 .grid(row=12, column=6, pady = 10)
        btnChange13 = Button(self.cvs, text="13", width=200, command=lambda: self.controller.show_frame(PageTwo),)
        btnChange13 .grid(row=13, column=6, pady = 10)
        btnChange14 = Button(self.cvs, text="14", width=200, command=lambda: self.controller.show_frame(PageTwo),)
        btnChange14 .grid(row=14, column=6, pady = 10)

        self.cvs.pack()

        def change_page(self):
            pass


class PageTwo(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller  
        ttk.Frame.__init__(self, parent)
        self.make_widget()

    def make_widget(self):
        self.cvs = Canvas(self, width="800", height="600", background="#7F7FD5")
        # Обучени
        button1 = ttk.Button(self, text='Обучение',  command=lambda: self.controller.show_frame(PageThree))
        button1.place(x=400, y=300, width="500", height="60")
        # Контроль
        button2 = ttk.Button(self, text='Контроль', command=lambda: self.controller.show_frame(PageFour))
        button2.place(x=400, y=400, width="500", height="60")
        button1 = ttk.Button(self, text='Назад', command=lambda: self.controller.show_frame(PageOne))
        button1.grid()

class PageThree(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller  
        ttk.Frame.__init__(self, parent)
        self.make_widget()

    def make_widget(self):
        button3 = ttk.Button(self, text='Назад',
                             command=lambda: self.controller.show_frame(PageTwo))
        button3.grid()

class PageFour(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller  
        ttk.Frame.__init__(self, parent)
        self.make_widget()

    def make_widget(self):
        button1 = ttk.Button(self, text='Назад',
                             command=lambda: self.controller.show_frame(PageTwo))
        button1.grid()

if __name__ == '__main__':
    app = MyApp()
    app.title('Лабораторный практикум')
    app.attributes ('-fullscreen' True)
    app.mainloop()