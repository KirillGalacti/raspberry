# import eel

# eel.init("web")

# @eel.expose
# def new_window(target: str):
#     eel.show(f"html/{target}")

# eel.start('index.html', size=(1000, 700), port = 8000)
# eel.show("main.html", size=(1000, 700), port = 8000)
# eel.show("learn.html", size=(1000, 700), port = 8000)
# eel.show("test.html", size=(1000, 700), port = 8000)

from tkinter import *
import tkinter.ttk as ttk


class MyApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.frames = {}
        for F in (PageOne, PageTwo, PageThree, PageFour):
            frame = F(container, self)
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

    def make_widget(self):
        self.cvs = Canvas(self, width="800", height="600", background="#7F7FD5")

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

# from tkinter import *
# from tkinter import messagebox
 
# def calculate_bmi():
#    kg = int(weight_tf.get())
#    m = int(height_tf.get())/100
#    bmi = kg/(m*m)
#    bmi = round(bmi, 1)
 
#    if bmi < 18.5:
#        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует недостаточному весу')
#    elif (bmi > 18.5) and (bmi < 24.9):
#        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует нормальному весу')
#    elif (bmi > 24.9) and (bmi < 29.9):
#        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует избыточному весу')
#    else:
#        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует ожирению')  
 
# window = Tk()
# window.title('Лабораторный практикум')
# window.geometry('400x300')
 
 
# frame = Frame(
#    window,
#    padx=10,
#    pady=10
# )
# frame.pack(expand=True)
 
 
# height_lb = Label(
#    frame,
#    text="Введите свой рост (в см)  "
# )
# height_lb.grid(row=3, column=1)
 
# weight_lb = Label(
#    frame,
#    text="Введите свой вес (в кг)  ",
# )
# weight_lb.grid(row=4, column=1)
 
# height_tf = Entry(
#    frame,
# )
# height_tf.grid(row=3, column=2, pady=5)
 
# weight_tf = Entry(
#    frame,
# )
# weight_tf.grid(row=4, column=2, pady=5)
 
# cal_btn = Button(
#    frame,
#    text='Рассчитать ИМТ',
#    command=calculate_bmi
# )
# cal_btn.grid(row=5, column=2)
 
# window.mainloop()