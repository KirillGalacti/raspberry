from tkinter import *
import RPi.GPIO as IO

"""Setup the GPIO Pins"""
IO.setmode(IO.BCM)
IO.setup(5,IO.IN)
IO.setup(6,IO.IN)

while True
def buttonPressed1(channel):
    """This function should be called when GPIO 7 has a rising edge event"""
    global enabled1
    print("Button was pressed")
    enabled1.set(True)
def buttonPressed2(channel):
    """This function should be called when GPIO 7 has a rising edge event"""
    global enabled2
    print("Button was pressed")
    enabled2.set(True)

"""Register the callback"""
IO.add_event_detect(5, IO.RISING, callback=buttonPressed1)
IO.add_event_detect(6, IO.RISING, callback=buttonPressed2)

root = Tk()
root.title("TEST")
root.geometry("250x200")

enabled1 = BooleanVar()
  
enabled_checkbutton1 = ttk.Checkbutton(text="Включить", variable=enabled1)
enabled_checkbutton1.pack(padx=6, pady=6, anchor=NW)
  
enabled_label1 = ttk.Label(textvariable=enabled1)
enabled_label1.pack(padx=6, pady=6, anchor=NW)

enabled2 = BooleanVar()
  
enabled_checkbutton2 = ttk.Checkbutton(text="Включить", variable=enabled2)
enabled_checkbutton2.pack(padx=6, pady=6, anchor=NW)
  
enabled_label2 = ttk.Label(textvariable=enabled2)
enabled_label2.pack(padx=6, pady=6, anchor=NW)
 
root.mainloop()