# from tkinter import *
# from tkinter import Tk, W, E
# from tkinter.ttk import Frame, Button, Entry, Style
# import tkinter as ttk
# import tkinter as os

# class app():
#     def __init__(self, master):
#         self.window = ttk.Tk()
#         # self.fullScreenState = True
#         # self.window.attributes("-fullscreen", self.fullScreenState)

#         # self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
#         # self.window.geometry("%dx%d" % (self.w, self.h))
        
#         # self.window.bind("<F11>", self.toggleFullScreen)
#         # self.window.bind("<Escape>", self.quitFullScreen)

#         self.startPage()

#     # Основное приложение
#     def startPage(self):
#         scrollbar = Scrollbar(root)
#         scrollbar.pack( side = RIGHT, fill = Y )
        
#         for i in self.window.winfo_children():
#             i.destroy()
#         self.frame1 = Frame(self.window)
#         self.frame1.pack()
#         self.label = ttk.Label(self.frame1, text='Старт')
#         self.label.pack()

#         self.buttons = []
#         for i in range(10):
#                 self.buttons.append(ttk.Button(self.frame1, text="Button " + str(i), command = self.choicePage))
#                 self.buttons[-1].pack()
    
#     def choicePage(self):
#         for i in self.window.winfo_children():
#             i.destroy()
#         self.frame2 = Frame(self.window)
#         self.frame2.pack()
#         self.choice_txt2 = ttk.Label(self.frame2, text='register')
#         self.choice_txt2.pack()
#         self.learn_btn = ttk.Button(self.frame2, text="Обучение", command=self.learnPage)
#         self.learn_btn.pack()
#         self.test_btn = ttk.Button(self.frame2, text="Контроль", command=self.testPage)
#         self.test_btn.pack()
#         self.back_btn = ttk.Button(self.frame2, text="Назад", command=self.startPage)
#         self.back_btn.pack()

#     def learnPage(self):
#         for i in self.window.winfo_children():
#             i.destroy()
#         self.frame3 = Frame(self.window)
#         self.frame3.pack()
#         self.learn_txt2 = ttk.Label(self.frame3, text='Обучение')
#         self.learn_txt2.pack()
#         self.back_btn = ttk.Button(self.frame3, text="Назад", command=self.choicePage)
#         self.back_btn.pack()
#         self.test_btn = ttk.Button(self.frame3, text="Пройти контроль", command=self.testPage)
#         self.test_btn.pack()

#     def testPage(self):
#         for i in self.window.winfo_children():
#             i.destroy()
#         self.frame4 = Frame(self.window)
#         self.frame4.pack()
#         self.test_txt2 = ttk.Label(self.frame4, text='Контроль')
#         self.test_txt2.pack()
#         self.back_btn = ttk.Button(self.frame4, text="Назад", command=self.choicePage)
#         self.back_btn.pack()
        
#     # Полноэкранный режим
#     def toggleFullScreen(self, event):
#         self.fullScreenState = not self.fullScreenState
#         self.window.attributes("-fullscreen", self.fullScreenState)

#     def quitFullScreen(self, event):
#          self.fullScreenState = False
#          self.window.attributes("-fullscreen", self.fullScreenState)

# root = Tk()
# app(root)
# root.title("Лабораторный практикум")
# root.attributes('-alpha', True)
# root.mainloop()

from tkinter import *
from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Entry, Style
from tkPDFViewer import tkPDFViewer as pdf
import tkinter as ttk
import tkinter as os


class MyApp:

    def __init__(self):
        # scrollbar = Scrollbar(root)
        # scrollbar.pack( side = RIGHT, fill = Y )
        self.tk = Tk()
        self.tk.attributes('-fullscreen', True)  # This just maximizes it so we can see the window. It nothing to do with fullscreen.
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)

        self.startPage()

    # Основное приложение
    def startPage(self):
        
        for i in self.tk.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.tk)
        self.frame1.pack()
        self.label = ttk.Label(self.frame1, text='Старт', foreground="white", background="black" )
        self.label.pack()

        self.buttons = []
        for i in range(10):
                self.buttons.append(ttk.Button(self.frame1, text="Button " + str(i), command = self.choicePage))
                self.buttons[-1].pack()
    
    def choicePage(self):
        for i in self.tk.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.tk)
        self.frame2.pack()
        self.choice_txt2 = ttk.Label(self.frame2, text='Выбор')
        self.choice_txt2.pack()
        self.learn_btn = ttk.Button(self.frame2, text="Обучение", command=self.learnPage)
        self.learn_btn.pack()
        self.test_btn = ttk.Button(self.frame2, text="Контроль", command=self.testPage)
        self.test_btn.pack()
        self.back_btn = ttk.Button(self.frame2, text="Назад", command=self.startPage)
        self.back_btn.pack()

    def learnPage(self):
        for i in self.tk.winfo_children():
            i.destroy()
        self.frame3 = Frame(self.tk)
        self.frame3.pack()
        self.learn_txt2 = ttk.Label(self.frame3, text='Обучение')
        self.learn_txt2.pack()
        self.back_btn = ttk.Button(self.frame3, text="Назад", command=self.choicePage)
        self.back_btn.pack()
        self.test_btn = ttk.Button(self.frame3, text="Пройти контроль", command=self.testPage)
        self.test_btn.pack()

    def testPage(self):
        for i in self.tk.winfo_children():
            i.destroy()
        self.frame4 = Frame(self.tk)
        self.frame4.pack()
        self.test_txt2 = ttk.Label(self.frame4, text='Контроль')
        self.test_txt2.pack()
        self.back_btn = ttk.Button(self.frame4, text="Назад", command=self.choicePage)
        self.back_btn.pack()

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

if __name__ == '__main__':
    root = Tk()
    w = MyApp()
    w.tk.mainloop()