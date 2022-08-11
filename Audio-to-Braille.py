import speech_recognition as sr
import time
import shutil
import os
from pydub import AudioSegment
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
    
    def file_man(self,frame_class):
        os.popen("orca")
        os.popen("sudo pcmanfm /media/MIMOBraille/")
        app.checker()
        
    def checker(self):
        if not os.listdir('/media/MIMOBraille/Speech Transcription Output'):
            time.sleep(2)
            app.checker()
        else:
            os.popen("sudo pkill pcmanfm")
            app.copy()
    
    def copy(self):
        for file in os.listdir("/media/MIMOBraille/Speech Transcription Output/"):
            new_name = r"/media/MIMOBraille/Speech Transcription Output/output.mp3"
            os.rename(os.path.join("/media/MIMOBraille/Speech Transcription Output/", file), new_name)
            original = r"/media/MIMOBraille/Speech Transcription Output/output.mp3"
            target = r"/home/MIMOBraille/Desktop/MIMOBraille/output.mp3"
            shutil.copyfile(original, target)
            app.main(1)

    def main(self,frame_class):
        sound = AudioSegment.from_mp3("/home/MIMOBraille/Desktop/MIMOBraille/output.mp3")
        sound.export("/home/MIMOBraille/Desktop/MIMOBraille/output.wav", format="wav")
                                                     
        AUDIO_FILE = "/home/MIMOBraille/Desktop/MIMOBraille/output.wav"
                                      
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)
        try:
            transcription=r.recognize_google(audio,language = 'en-US')
            transcript=open("/home/MIMOBraille/Desktop/MIMOBraille/output.txt","w")
            transcript.write(transcription)
            transcript.close()
            twidget=tk.Text(self,height = 10, width = 45)
            sbar=tk.Scrollbar(self)
            sbar.pack(side=tk.RIGHT)
            twidget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            twidget.insert(tk.END,transcription)
            app.distributor(1)
            app.closer()
            clear()
        except sr.UnknownValueError:
            tk.Label(self, text="Google Speech Recognition could not understand audio",height = 3, width = 45, bg='light pink', font=("bold",10),wraplength=480).pack(side="top", fill="x", pady=10)
            os.system("ffplay -autoexit -nodisp "+"/home/MIMOBraille/Desktop/MIMOBraille/UI-Sounds/Google Speech Recognition.mp3")
            clear()
            app.quit_button_pressed(1)
        except sr.RequestError:
            tk.Label(self, text="Could not request results from Google Speech Recognition service",height = 3, width = 45, bg='light pink', font=("bold",10),wraplength=480).pack(side="top", fill="x", pady=10)
            os.system("ffplay -autoexit -nodisp "+"/home/MIMOBraille/Desktop/MIMOBraille/UI-Sounds/Could_not_request.mp3")
            clear()
            app.quit_button_pressed(1)

class SpeechBraille(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Press Button 1, to browse for audio file...", height = 1, width = 45, font=("bold")).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Browse Audio File", height = 1, width = 60, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: app.file_man(1)).pack()
        tk.Button(self, text="Return to speech input selection", height = 1, width = 60, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: app.quit_button_pressed(1)).pack()

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(12,GPIO.RISING,callback=app.file_man,bouncetime=200)
    GPIO.add_event_detect(13,GPIO.RISING,callback=app.quit_button_pressed,bouncetime=200)

def clear():
    for root, dirs, files in os.walk('/media/MIMOBraille/Speech Transcription Output'):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))

if __name__ == "__main__":
    app = MIMOBraille()
    app.title("Audio File to Braille")
    setup()
    clear()
    app.mainloop()

