import subprocess
import time
from tkinter import *


# this function suspends GTA5.exe process for 10 seconds to "kick" all players
def privatesessionmaker():
    subprocess.run(["pssuspend.exe", "GTA5.exe"])
    time.sleep(10)
    subprocess.run(["pssuspend.exe", "-r", "GTA5.exe"])

def click():
    privatesessionmaker()
    button.config(state="disabled", text="Private Session created successfully! You may exit now ...")
    
# Button

window = Tk()

button = Button(window,
                text="Click and wait 10 seconds",
                command=click,
                font=("Comic Sans", 45),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                compound='bottom')
button.pack()

window.mainloop()
