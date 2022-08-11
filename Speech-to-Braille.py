import speech_recognition as sr
import time
import os
from time import sleep
import RPi.GPIO as GPIO
import tkinter as tk
from tkinter import *

class MIMOBraille(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(SpeechBraille)
        self.geometry('480x320')

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()  
    
    def distributor(self,frame_class):
        cell=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/BrailleMode")
        distribmode=int(cell.read())
        
        if distribmode==0:
            os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Distributor_Auto.py')
        
        elif distribmode==1:
            os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Distributor.py')
            
    def quit_button_pressed(self,channel):
        GPIO.cleanup()
        os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/S2B_Selector.py')
        app.destroy()
        quit()
    
    def closer(self):
        closer=0
        while closer==0:
            time.sleep(1)
            check=open("/home/MIMOBraille/Desktop/MIMOBraille/output.txt", "r", encoding="utf-8-sig")
            if check.read()=="":
                app.destroy()
                closer=1
        
    def main(self,frame_class):
        os.system("ffplay -autoexit -nodisp "+"/home/MIMOBraille/Desktop/MIMOBraille/UI-Sounds/Beep.mp3")
        r = sr.Recognizer()
        speech = sr.Microphone(device_index=0)
        with speech as source:
            audio = r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            recog = r.recognize_google(audio, language="en-US")
            f=open("/home/MIMOBraille/Desktop/MIMOBraille/output.txt","w")
            f.write(recog)
            f.close()
            twidget=tk.Text(self,height = 10, width = 45)
            sbar=tk.Scrollbar(self)
            sbar.pack(side=tk.RIGHT)
            twidget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            twidget.insert(tk.END,recog)
            time.sleep(.1)
            app.distributor(1)
            app.closer()
        except sr.UnknownValueError:
            tk.Label(self, text="Google Speech Recognition could not understand audio",height = 3, width = 45, bg='light pink', font=("bold",10),wraplength=480).pack(side="top", fill="x", pady=10)
            os.system("ffplay -autoexit -nodisp "+"/home/MIMOBraille/Desktop/MIMOBraille/UI-Sounds/Google Speech Recognition.mp3")
        except sr.RequestError:
            tk.Label(self, text="Could not request results from Google Speech Recognition service",height = 3, width = 45, bg='light pink', font=("bold",10),wraplength=480).pack(side="top", fill="x", pady=10)
            os.system("ffplay -autoexit -nodisp "+"/home/MIMOBraille/Desktop/MIMOBraille/UI-Sounds/Could_not_request.mp3")
            
class SpeechBraille(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Press Button 1,then say something...", height = 1, width = 45, font=("bold")).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Start Speaking", height = 1, width = 60, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: app.main(1)).pack()
        tk.Button(self, text="Return to speech input selection", height = 1, width = 60, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: app.quit_button_pressed(1)).pack()
        
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(12,GPIO.RISING,callback=app.main,bouncetime=200)
    GPIO.add_event_detect(13,GPIO.RISING,callback=app.quit_button_pressed,bouncetime=200)


if __name__ == "__main__":
    app = MIMOBraille()
    setup()
    app.mainloop()
