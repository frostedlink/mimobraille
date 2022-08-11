import time
import os
import RPi.GPIO as GPIO
import tkinter as tk
from tkinter import *
from gtts import gTTS

class MIMOBraille(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(DirectEdit)
        self.geometry('480x320')

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def close(self):
        app.destroy()
    
    def quit_button_pressed(self,channel):
        GPIO.cleanup()
        os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/T2B_Selector.py')
        app.close()
        quit()
    
    def editor(self,frame_class):
        os.system("ffplay -autoexit -nodisp "+"/home/MIMOBraille/Desktop/MIMOBraille/UI-Sounds/Beep.mp3")
        os.popen("orca")
        os.popen("mousepad /home/MIMOBraille/Desktop/MIMOBraille/output.txt")
        app.checker()
    
    def checker(self):
        f=open("/home/MIMOBraille/Desktop/MIMOBraille/output.txt","r",encoding="utf-8-sig")
        if f.read()=="":
            time.sleep(2)
            app.checker()
        else:
            os.popen("sudo pkill orca")
            os.popen("sudo pkill mousepad")
            time.sleep(5)
            app.main(1)
    
    def main(self,frame_class):
        f=open("/home/MIMOBraille/Desktop/MIMOBraille/output.txt","r",encoding="utf-8-sig")
        textwritten=f.read()
        twidget=tk.Text(self,height = 10, width = 45)
        sbar=tk.Scrollbar(self)
        sbar.pack(side=tk.RIGHT)
        twidget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        twidget.insert(tk.END,textwritten)
        language = 'en'
        writtentext=gTTS(text=textwritten, lang=language, slow=True)
        writtentext.save("/home/MIMOBraille/Desktop/MIMOBraille/braille-output.mp3")
        time.sleep(1)
        os.system("ffplay -autoexit -nodisp "+"/home/MIMOBraille/Desktop/MIMOBraille/braille-output.mp3")
        app.quit_button_pressed(1)
        
class DirectEdit(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Press Button 1, to start typing...", height = 1, width = 45, font=("bold")).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Start Typing", height = 1, width = 60, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: app.editor(1)).pack()
        tk.Button(self, text="Return to type input selection", height = 1, width = 60, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: app.quit_button_pressed(1)).pack()

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(12,GPIO.RISING,callback=app.editor,bouncetime=200)
    GPIO.add_event_detect(13,GPIO.RISING,callback=app.quit_button_pressed,bouncetime=200)
    clear=""
    f=open("/home/MIMOBraille/Desktop/MIMOBraille/output.txt","w")
    f.write(clear)
    
    
    
if __name__ == "__main__":
    app = MIMOBraille()
    app.title("Type to Speech")
    setup()
    app.mainloop()
        
        
