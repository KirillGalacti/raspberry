import RPi.GPIO as GPIO
from tkinter import *
from gpiozero import Button
from tkinter import messagebox as mb
import json

GPIO.setup(26, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(5, GPIO.IN)

class Quiz:
    def __init__(self):
        self.q_no = 0
        self.display_title()
        self.display_question()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.data_size = len(question)
        self.correct = 0

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Правильно: {self.correct}"
        wrong = f"Неправильно: {wrong_count}"
         
        score = int(self.correct / self.data_size * 100)
        result = f"Счет: {score}%"
         
        mb.showinfo("Результат", f"{result}\n{correct}\n{wrong}")
    
    def check_answer(self, q_on):
        if self.opt_selected.get() ==[q_no]
            return True

    def next_btn(self):
        if self.check_answer(self.q_no):
            self.correct += 1
        self.q_no += 1
        if self.q_no == self.data_size:
            self.display_result()
        else:
            self.display_question()
            self.display_opyions()

    def sensor_next_btn(self):
        if self.check_answer(GPIO.input(16) == True):
            self.correct += 1
        self.q_no += 1
        if self.q_no == self.data_size:
            self.display_result()
        else:
            self.display_question()
            self.display_opyions()
    def buttons(self):
         
        next_button = Button(gui, text="Дальше",command=self.next_btn,
        width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
         
        next_button.place(x=350,y=380)
         
        quit_button = Button(gui, text="Выход", command=gui.destroy,
        width=5,bg="black", fg="white",font=("ariel",16," bold"))
         
        quit_button.place(x=700,y=50)

    def display_options(self):
        val=0

        self.opt_selected.set(0)
         
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1

     def display_question(self):

        q_no = Label(gui, text=question[self.q_no], width=60, font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
        q_no.place(x=70, y=100)
 
    def display_title(self):
        title = Label(gui, text="...", width=50, bg="green",fg="white", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)
 
    def radio_buttons(self):
        q_list = []
        y_pos = 150            
        radio_btn_1 = Radiobutton(gui,text=" ",variable=self.opt_selected, value = len(q_list)+1,font = ("ariel",14))           
        q_list.append(radio_btn)
        radio_btn.place(x = 100, y = y_pos)     
        y_pos += 40
    
    def sensor_button(self):
        if()

gui = Tk()
gui.geometry("800x450")
gui.title("Контроль")
 
with open('data.json') as f:
    data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])
 

quiz = Quiz()
gui.mainloop()

