from tkinter import *
import RPi.GPIO as IO

"""Setup the GPIO Pins"""
IO.setmode(IO.BCM)
IO.setup(5,IO.IN)
IO.setup(6,IO.IN)
IO.setup(13,IO.IN)

while True
def buttonPressed(channel):
    """This function should be called when GPIO 7 has a rising edge event"""
    global enable
    print("Button was pressed")
    enable.set(enable.get() + 1)

"""Register the callback"""
IO.add_event_detect(5, IO.RISING, callback=buttonPressed)

root = Tk()
root.title("TEST")
root.geometry("250x200")

enabled = IntVar()
  
enabled_checkbutton = ttk.Checkbutton(text="Включить", variable=enabled)
enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)
  
enabled_label = ttk.Label(textvariable=enabled)
enabled_label.pack(padx=6, pady=6, anchor=NW)
 
root.mainloop()