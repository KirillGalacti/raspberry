from tkinter import *
import RPi.GPIO as IO

"""Setup the GPIO Pins"""
IO.setmode(IO.BCM)
IO.setup(5,IO.IN)

def buttonPressed(channel):
    """This function should be called when GPIO 7 has a rising edge event"""
    global var
    print("Button was pressed")
    var.set(var.get() + 1)
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
 
enabled = IntVar()
  
enabled_checkbutton = ttk.Checkbutton(text="Включить", variable=enabled)
enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)
  
enabled_label = ttk.Label(textvariable=enabled)
enabled_label.pack(padx=6, pady=6, anchor=NW)
 
root.mainloop()