import os
import tkinter as tk
import RPi.GPIO as GPIO
from tkinter import *

class MIMOBraille(tk.Tk):
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(12,GPIO.RISING,callback=app.quit_button_pressed,bouncetime=500)
        GPIO.add_event_detect(13,GPIO.RISING,callback=app.shutdown,bouncetime=500)
        os.system("ffplay -autoexit -nodisp "+"/home/MIMOBraille/Desktop/MIMOBraille/UI-Sounds/Shutdown.mp3")
        
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(TypeFrame)
        self.geometry('480x320')

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        
    def close(self):
        GPIO.cleanup()
        app.destroy()
    
    def quit_button_pressed(self,channel):
        GPIO.cleanup()
        os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Main-Program.py')
        app.close()
        quit()
    
    def shutdown(self, frame_class):
        os.popen ('sudo shutdown -P now')

class TypeFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Are you sure you want to quit? Press button 1 to return to main menu, press button 5 to shutdown", height = 2, width = 50, font=("bold"),wraplength=480).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to Main Menu", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: app.quit_button_pressed(1)).pack()
        tk.Button(self, text="Shutdown", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: app.shutdown(1)).pack()

if __name__ == "__main__":
    app = MIMOBraille()
    app.title("Shutdown?")
    app.setup()
    app.mainloop()


