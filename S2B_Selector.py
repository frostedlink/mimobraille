import os
import tkinter as tk
import RPi.GPIO as GPIO
from tkinter import *

class MIMOBraille(tk.Tk):
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(12,GPIO.RISING,callback=app.speech,bouncetime=500)
        GPIO.add_event_detect(16,GPIO.RISING,callback=app.audio,bouncetime=500)
        GPIO.add_event_detect(13,GPIO.RISING,callback=app.quit_button_pressed,bouncetime=500)
        os.system("ffplay -autoexit -nodisp "+"/home/MIMOBraille/Desktop/MIMOBraille/UI-Sounds/Speech_to_Braille.mp3")
        os.popen("sudo pkill orca")
        
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(SpeechAudio)
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
        
    def audio(self, frame_class):
        os.popen ('orca')
        GPIO.cleanup()
        os.system("ffplay -autoexit -nodisp "+"/home/MIMOBraille/Desktop/MIMOBraille/UI-Sounds/Audio_File_Input.mp3")
        os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Audio-to-Braille.py')
        app.destroy()
    
    def speech(self, frame_class):
        GPIO.cleanup()
        os.system("ffplay -autoexit -nodisp "+"/home/MIMOBraille/Desktop/MIMOBraille/UI-Sounds/Microphone.mp3")
        os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Speech-to-Braille.py')
        app.destroy()

class SpeechAudio(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Press button 1 to select Live speech to braille, press button 2 to select audio file  to braille...", height = 3, width = 50, font=("bold"), wraplength=480).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Live speech to Braille", height = 2, width = 60, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: app.speech(1)).pack()
        tk.Button(self, text="Audio File to Braille", height = 2, width = 60, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: app.audio(1)).pack()
        tk.Button(self, text="Return to start page", height = 2, width = 60, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: app.quit_button_pressed(1)).pack()

if __name__ == "__main__":
    app = MIMOBraille()
    app.title("Speech to Braille")
    app.setup()
    app.mainloop()