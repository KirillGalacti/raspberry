from tkinter import *
from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Entry, Style
import tkinter as ttk
import tkinter as os

class MyApp:
    def __init__(self, master):
        self.window = ttk.Tk()
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

        self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (self.w, self.h))
        
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)

        self.startPage()
        
    # Стартовая страница с выбором желаемой лабораторной работы
    def startPage(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.make_widget_startPage()

    def make_widget_startPage(self):
        Style().configure("TButton", padding=(0, 20, 0, 20), font='serif 10')

        self.cvs = Canvas(self, width="800", height="600", background="#7F7FD5")

        # demo button to change page
        btnChange1 = Button(self.cvs, text="1", width=200, command=lambda: self.choicePage)
        btnChange1 .grid(row=1, column=6, pady = 10)
        btnChange2 = Button(self.cvs, text="2", width=200, command=lambda: self.choicePage)
        btnChange2 .grid(row=2, column=6, pady = 10)
        btnChange3 = Button(self.cvs, text="3", width=200, command=lambda: self.choicePage)
        btnChange3 .grid(row=3, column=6, pady = 10)
        btnChange4 = Button(self.cvs, text="4", width=200, command=lambda: self.choicePage)
        btnChange4 .grid(row=4, column=6, pady = 10)
        btnChange5 = Button(self.cvs, text="5", width=200, command=lambda: self.choicePage)
        btnChange5 .grid(row=5, column=6, pady = 10)
        btnChange6 = Button(self.cvs, text="6", width=200, command=lambda: self.choicePage)
        btnChange6 .grid(row=6, column=6, pady = 10)
        btnChange7 = Button(self.cvs, text="7", width=200, command=lambda: self.choicePage)
        btnChange7 .grid(row=7, column=6, pady = 10)
        btnChange8 = Button(self.cvs, text="8", width=200, command=lambda: self.choicePage)
        btnChange8 .grid(row=8, column=6, pady = 10)
        btnChange9 = Button(self.cvs, text="9", width=200, command=lambda: self.choicePage)
        btnChange9 .grid(row=9, column=6, pady = 10)
        btnChange10 = Button(self.cvs, text="10", width=200, command=lambda: self.choicePage)
        btnChange10 .grid(row=10, column=6, pady = 10)
        btnChange11 = Button(self.cvs, text="11", width=200, command=lambda: self.choicePage)
        btnChange11 .grid(row=11, column=6, pady = 10)
        btnChange12 = Button(self.cvs, text="12", width=200, command=lambda: self.choicePage)
        btnChange12 .grid(row=12, column=6, pady = 10)
        btnChange13 = Button(self.cvs, text="13", width=200, command=lambda: self.choicePage)
        btnChange13 .grid(row=13, column=6, pady = 10)
        btnChange14 = Button(self.cvs, text="14", width=200, command=lambda: self.choicePage)
        btnChange14 .grid(row=14, column=6, pady = 10)

        self.cvs.pack()
    
    # Страница с выбором режима
    def choicePage(self, parent, controller):
        self.controller = controller  
        ttk.Frame.__init__(self, parent)
        self.make_widget_choicePage()

    def make_widget_choicePage(self):
        self.cvs = Canvas(self, width="800", height="600", background="#7F7FD5")
        # Обучени
        button1 = ttk.Button(self, text='Обучение')
        button1.place(x=400, y=300, width="500", height="60")
        # Контроль
        button2 = ttk.Button(self, text='Контроль')
        button2.place(x=400, y=400, width="500", height="60")
        button1 = ttk.Button(self, text='Назад', command=lambda: self.choicePage)
        button1.grid()
    
    # Полноэкранный режим
    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

root = Tk()
MyApp(root)
root.title("Лабораторный практикум")
root.mainloop()

# class Scrollbar(ttk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.scroll_x = ttk.Scrollbar(self, orient=ttk.HORIZONTAL)
#         self.scroll_y = ttk.Scrollbar(self, orient=ttk.VERTICAL)
#         self.canvas = ttk.Canvas(self, width=300, height=100,
#                                 xscrollcommand=self.scroll_x.set,
#                                 yscrollcommand=self.scroll_y.set)
#         self.scroll_x.config(command=self.canvas.xview)
#         self.scroll_y.config(command=self.canvas.yview)

#         self.scroll_x.grid(row=1, column=0, sticky="we")
#         self.scroll_y.grid(row=0, column=1, sticky="ns")

#         self.rowconfigure(0, weight=1)
#         self.columnconfigure(0, weight=1)
#         self.update_idletasks()
#         self.minsize(self.winfo_width(), self.winfo_height())

#     def resize(self, event):
#         region = self.canvas.bbox(ttk.ALL)
#         self.canvas.configure(scrollregion=region)

# class MyApp(Tk):
#     def __init__(self):
#         Tk.__init__(self)
#         container = ttk.Frame(self)
#         # self.window = ttk.Tk()
#         # self.fullScreenState = False
#         # self.window.attributes("-fullscreen", True)

#         # self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
#         # self.window.geometry("%dx%d" % (self.w, self.h))
        
#         # self.window.bind("<F11>", self.toggleFullScreen)
#         # self.window.bind("<Escape>", self.quitFullScreen)

#         container.pack(side="top", fill="both", expand=True)
#         self.frames = {}
#         for F in (PageOne, PageTwo, PageThree, PageFour):
#             frame = F(container, self)
#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky='NSEW')
#         self.show_frame(PageOne)

#     def show_frame(self, cont):
#         frame = self.frames[cont]
#         frame.tkraise()

#     def toggleFullScreen(self, event):
#         self.fullScreenState = not self.fullScreenState
#         self.window.attributes("-fullscreen", self.fullScreenState)

#     def quitFullScreen(self, event):
#         self.fullScreenState = False
#         self.window.attributes("-fullscreen", self.fullScreenState)

# class PageOne(ttk.Frame):
#     def __init__(self, parent, controller):
#         self.controller = controller
#         ttk.Frame.__init__(self, parent)
#         self.make_widget()

#     def open_file():
#         os.system()

#     def make_widget(self):
#         Style().configure("TButton", padding=(0, 20, 0, 20), font='serif 10')

#         self.cvs = Canvas(self, width="800", height="600", background="#7F7FD5")

#         # demo button to change page
#         btnChange1 = Button(self.cvs, text="1", width=200, command=lambda: self.controller.show_frame(PageTwo))
#         btnChange1 .grid(row=1, column=6, pady = 10)
#         btnChange2 = Button(self.cvs, text="2", width=200, command=lambda: self.controller.show_frame(PageTwo))
#         btnChange2 .grid(row=2, column=6, pady = 10)
#         btnChange3 = Button(self.cvs, text="3", width=200, command=lambda: self.controller.show_frame(PageTwo))
#         btnChange3 .grid(row=3, column=6, pady = 10)
#         btnChange4 = Button(self.cvs, text="4", width=200, command=lambda: self.controller.show_frame(PageTwo))
#         btnChange4 .grid(row=4, column=6, pady = 10)
#         btnChange5 = Button(self.cvs, text="5", width=200, command=lambda: self.controller.show_frame(PageTwo),)
#         btnChange5 .grid(row=5, column=6, pady = 10)
#         btnChange6 = Button(self.cvs, text="6", width=200, command=lambda: self.controller.show_frame(PageTwo),)
#         btnChange6 .grid(row=6, column=6, pady = 10)
#         btnChange7 = Button(self.cvs, text="7", width=200, command=lambda: self.controller.show_frame(PageTwo),)
#         btnChange7 .grid(row=7, column=6, pady = 10)
#         btnChange8 = Button(self.cvs, text="8", width=200, command=lambda: self.controller.show_frame(PageTwo),)
#         btnChange8 .grid(row=8, column=6, pady = 10)
#         btnChange9 = Button(self.cvs, text="9", width=200, command=lambda: self.controller.show_frame(PageTwo),)
#         btnChange9 .grid(row=9, column=6, pady = 10)
#         btnChange10 = Button(self.cvs, text="10", width=200, command=lambda: self.controller.show_frame(PageTwo),)
#         btnChange10 .grid(row=10, column=6, pady = 10)
#         btnChange11 = Button(self.cvs, text="11", width=200, command=lambda: self.controller.show_frame(PageTwo),)
#         btnChange11 .grid(row=11, column=6, pady = 10)
#         btnChange12 = Button(self.cvs, text="12", width=200, command=lambda: self.controller.show_frame(PageTwo),)
#         btnChange12 .grid(row=12, column=6, pady = 10)
#         btnChange13 = Button(self.cvs, text="13", width=200, command=lambda: self.controller.show_frame(PageTwo),)
#         btnChange13 .grid(row=13, column=6, pady = 10)
#         btnChange14 = Button(self.cvs, text="14", width=200, command=lambda: self.controller.show_frame(PageTwo),)
#         btnChange14 .grid(row=14, column=6, pady = 10)

#         self.cvs.pack()

#         def change_page(self):
#             pass


# class PageTwo(ttk.Frame):
#     def __init__(self, parent, controller):
#         self.controller = controller  
#         ttk.Frame.__init__(self, parent)
#         self.make_widget()

#     def make_widget(self):
#         self.cvs = Canvas(self, width="800", height="600", background="#7F7FD5")
#         # Обучени
#         button1 = ttk.Button(self, text='Обучение',  command=lambda: self.controller.show_frame(PageThree))
#         button1.place(x=400, y=300, width="500", height="60")
#         # Контроль
#         button2 = ttk.Button(self, text='Контроль', command=lambda: self.controller.show_frame(PageFour))
#         button2.place(x=400, y=400, width="500", height="60")
#         button1 = ttk.Button(self, text='Назад', command=lambda: self.controller.show_frame(PageOne))
#         button1.grid()

# class PageThree(ttk.Frame):
#     def __init__(self, parent, controller):
#         self.controller = controller  
#         ttk.Frame.__init__(self, parent)
#         self.make_widget()

#     def make_widget(self):
#         button3 = ttk.Button(self, text='Назад',
#                              command=lambda: self.controller.show_frame(PageTwo))
#         button3.grid()

# class PageFour(ttk.Frame):
#     def __init__(self, parent, controller):
#         self.controller = controller  
#         ttk.Frame.__init__(self, parent)
#         self.make_widget()

#     def make_widget(self):
#         button1 = ttk.Button(self, text='Назад',
#                              command=lambda: self.controller.show_frame(PageTwo))
#         button1.grid()

# if __name__ == '__main__':
#     app = MyApp()
#     app.title('Лабораторный практикум')
#     #app.attributes('-fullscreen', True)
#     app.mainloop()

# from tkinter import *
# from tkinter import Tk, W, E
# from tkinter.ttk import Frame, Button, Entry, Style
# import tkinter as ttk
# import tkinter as os

# class VerticalScrolledFrame(ttk.Frame):
#     """A pure Tkinter scrollable frame that actually works!
#     * Use the 'interior' attribute to place widgets inside the scrollable frame.
#     * Construct and pack/place/grid normally.
#     * This frame only allows vertical scrolling.
#     """
#     def __init__(self, parent, *args, **kw):
#         ttk.Frame.__init__(self, parent, *args, **kw)

#         # Create a canvas object and a vertical scrollbar for scrolling it.
#         vscrollbar = ttk.Scrollbar(self, orient=VERTICAL)
#         vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
#         canvas = ttk.Canvas(self, bd=0, highlightthickness=0,
#                            yscrollcommand=vscrollbar.set)
#         canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
#         vscrollbar.config(command=canvas.yview)

#         # Reset the view
#         canvas.xview_moveto(0)
#         canvas.yview_moveto(0)

#         # Create a frame inside the canvas which will be scrolled with it.
#         self.interior = interior = ttk.Frame(canvas)
#         interior_id = canvas.create_window(0, 0, window=interior,
#                                            anchor=NW)

#         # Track changes to the canvas and frame width and sync them,
#         # also updating the scrollbar.
#         def _configure_interior(event):
#             # Update the scrollbars to match the size of the inner frame.
#             size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
#             canvas.config(scrollregion="0 0 %s %s" % size)
#             if interior.winfo_reqwidth() != canvas.winfo_width():
#                 # Update the canvas's width to fit the inner frame.
#                 canvas.config(width=interior.winfo_reqwidth())
#         interior.bind('<Configure>', _configure_interior)

#         def _configure_canvas(event):
#             if interior.winfo_reqwidth() != canvas.winfo_width():
#                 # Update the inner frame's width to fill the canvas.
#                 canvas.itemconfigure(interior_id, width=canvas.winfo_width())
#         canvas.bind('<Configure>', _configure_canvas)

# class app():
#     def __init__(self, master):
#         self.window = ttk.Tk()
#         self.fullScreenState = True
#         self.window.attributes("-fullscreen", self.fullScreenState)

#         self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
#         self.window.geometry("%dx%d" % (self.w, self.h))
        
#         self.window.bind("<F11>", self.toggleFullScreen)
#         self.window.bind("<Escape>", self.quitFullScreen)

#         self.startPage()

#     # Основное приложение
#     def startPage(self):
#         for i in self.window.winfo_children():
#             i.destroy()
#         self.frame1 = Frame(self.window)
#         self.frame1.pack()
#         self.label = ttk.Label(self.frame1, text='Старт')
#         self.label.pack()
#         Style().configure("TButton", padding=(0, 20, 0, 20), font='serif 10')
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
#         self.test_btn = ttk.Button(self.frame1, text="Контроль", command=self.testPage)
#         self.test_btn.pack()
#         self.back_btn = ttk.Button(self.frame3, text="Назад", command=self.choicePage)
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
# root.mainloop()