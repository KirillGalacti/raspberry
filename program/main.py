from tkinter import *
import tkinter.ttk as ttk


class MyApp(Tk):
    def __init__(self, master):
        Tk.__init__(self, master)
        container = ttk.Frame(self)
        master=ttk.master(self)
        container.pack(side="top", fill="both", expand=True)
        self.frames = {}
        for F in (PageOne, PageTwo, PageThree, PageFour):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='NSEW')
        self.show_frame(PageOne)
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom


class PageOne(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.make_widget()

    def make_widget(self):
        self.cvs = Canvas(self, background="#7F7FD5")

        # demo button to change page
        btnChange = Button(self.cvs, text="Какая-то лабораторная", font="Arial 16",
                           command=lambda: self.controller.show_frame(PageTwo),
                           bg="#a0ccda")
        btnChange .place(x=400, y=300, width="500", height="60")

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
        button1 = ttk.Button(self, text='Обучение',
                             command=lambda: self.controller.show_frame(PageThree))
        button1.place(x=400, y=300, width="500", height="60")
        # Контроль
        button2 = ttk.Button(self, text='Контроль',
                             command=lambda: self.controller.show_frame(PageFour))
        button2.place(x=400, y=300, width="500", height="60")

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
    app.mainloop()

