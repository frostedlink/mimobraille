import os
import tkinter as tk
import RPi.GPIO as GPIO
from tkinter import *

class MIMOBraille(tk.Tk):
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(12,GPIO.RISING,callback=app.typetobraille,bouncetime=500)
        GPIO.add_event_detect(16,GPIO.RISING,callback=app.typetospeech,bouncetime=500)
        GPIO.add_event_detect(13,GPIO.RISING,callback=app.quit_button_pressed,bouncetime=500)
        os.system("ffplay -autoexit -nodisp "+"/home/MIMOBraille/Desktop/MIMOBraille/UI-Sounds/Type_Inputs.mp3")
        
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
    
    def quit_button_pressed(self,channel):
        GPIO.cleanup()
        os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Main-Program.py')
        app.destroy()
        quit()
        
    def typetobraille(self, frame_class):
        GPIO.cleanup()
        os.system("ffplay -autoexit -nodisp "+"/home/MIMOBraille/Desktop/MIMOBraille/UI-Sounds/Type_to_Braille.mp3")
        os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Direct_Type.py')
        app.destroy()
    
    def typetospeech(self, frame_class):
        GPIO.cleanup()
        os.system("ffplay -autoexit -nodisp "+"/home/MIMOBraille/Desktop/MIMOBraille/UI-Sounds/Type_to_Speech.mp3")
        os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Text-to-Speech.py')
        app.destroy()

class TypeFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Press button 1 to select type to braille, press button 2 to select type to speech...", height = 3, width = 50, font=("bold"), wraplength=480).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Type to Braille", height = 2, width = 60, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: app.typetobraille(1)).pack()
        tk.Button(self, text="Type to Speech (Braille Keyboard)", height = 2, width = 60, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: app.typetospeech(1)).pack()
        tk.Button(self, text="Return to start page", height = 2, width = 60, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: app.quit_button_pressed(1)).pack()

if __name__ == "__main__":
    app = MIMOBraille()
    app.title("Type Inputs")
    app.setup()
    app.mainloop()

