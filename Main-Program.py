import time
import os
import tkinter as tk
import RPi.GPIO as GPIO
from tkinter import *

BrailleMode=0
BrailleSpeed=0
numberofCells=0
CameraBrightness=0
CameraSaturation=0
CameraSharpness=0

class MIMOBraille(tk.Tk):
    def setup(self):

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(20,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(12,GPIO.RISING,callback=app.SpeechSelector,bouncetime=500)
        GPIO.add_event_detect(13,GPIO.RISING,callback=app.quit_button_pressed,bouncetime=500)
        GPIO.add_event_detect(16,GPIO.RISING,callback=app.ImageSelector,bouncetime=500)
        GPIO.add_event_detect(19,GPIO.RISING,callback=app.exit,bouncetime=500)
        GPIO.add_event_detect(20,GPIO.RISING,callback=app.DigitalText,bouncetime=500)
        GPIO.add_event_detect(21,GPIO.RISING,callback=app.TypeSelector,bouncetime=500)
        
        clear=str("")
        f=open("/home/MIMOBraille/Desktop/MIMOBraille/output.txt","w",encoding="utf-8")
        f.write(clear)
        os.popen("sudo pkill orca")
        
        time.sleep(2)
        os.system("ffplay -autoexit -nodisp "+"/home/MIMOBraille/Desktop/MIMOBraille/UI-Sounds/Main_Menu.mp3")
    
    def ManualMode(self):
        global BrailleMode
        BrailleMode=1
        f=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/BrailleMode","w")
        f.write(str(BrailleMode))
    
    def AutoMode(self):
        global BrailleMode
        BrailleMode=0
        f=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/BrailleMode","w")
        f.write(str(BrailleMode))    
        
    def BSpeedIncrease(self):
        global BrailleSpeed
        Speed=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/BrailleSpeed", "r",encoding="utf-8-sig")
        BrailleSpeed=int(Speed.read())
        BrailleSpeed=BrailleSpeed+1
        f=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/BrailleSpeed","w")
        f.write(str(BrailleSpeed))
    
    def BSpeedDecrease(self):
        global BrailleSpeed
        Speed=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/BrailleSpeed", "r",encoding="utf-8-sig")
        BrailleSpeed=int(Speed.read())
        BrailleSpeed=BrailleSpeed-1
        f=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/BrailleSpeed","w")
        f.write(str(BrailleSpeed))
    
    def BCellIncrease(self):
        global numberofCells
        Speed=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/NumberOfCells", "r",encoding="utf-8-sig")
        numberofCells=int(Speed.read())
        numberofCells=numberofCells+1
        f=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/NumberOfCells","w")
        f.write(str(numberofCells))
    
    def BCellDecrease(self):
        global numberofCells
        Cells=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/NumberOfCells", "r",encoding="utf-8-sig")
        numberofCells=int(Cells.read())
        numberofCells=numberofCells-1
        f=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/NumberOfCells","w")
        f.write(str(numberofCells))
        
    def CameraBrightnessIncrease(self):
        global CameraBrightness
        Brightness=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/CameraBrightness", "r",encoding="utf-8-sig")
        CameraBrightness=int(Brightness.read())
        CameraBrightness=CameraBrightness+1
        f=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/CameraBrightness","w")
        f.write(str(CameraBrightness))
    
    def CameraBrightnessDecrease(self):
        global CameraBrightness
        Brightness=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/CameraBrightness", "r",encoding="utf-8-sig")
        CameraBrightness=int(Brightness.read())
        CameraBrightness=CameraBrightness-1
        f=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/CameraBrightness","w")
        f.write(str(CameraBrightness))
    
    def CameraSaturationIncrease(self):
        global CameraSaturation
        Saturation=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/CameraSaturation", "r",encoding="utf-8-sig")
        CameraSaturation=int(Saturation.read())
        CameraSaturation=CameraSaturation+1
        f=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/CameraSaturation","w")
        f.write(str(CameraSaturation))
    
    def CameraSaturationDecrease(self):
        global CameraSaturation
        Saturation=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/CameraSaturation", "r",encoding="utf-8-sig")
        CameraSaturation=int(Saturation.read())
        CameraSaturation=CameraSaturation-1
        f=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/CameraSaturation","w")
        f.write(str(CameraSaturation))
    
    def CameraSharpnessIncrease(self):
        global CameraSharpness
        Sharpness=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/CameraSharpness", "r",encoding="utf-8-sig")
        CameraSharpness=int(Sharpness.read())
        CameraSharpness=CameraSharpness+1
        f=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/CameraSharpness","w")
        f.write(str(CameraSharpness))
    
    def CameraSharpnessDecrease(self):
        global CameraSharpness
        Sharpness=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/CameraSharpness", "r",encoding="utf-8-sig")
        CameraSharpness=int(Sharpness.read())
        CameraSharpness=CameraSharpness-1
        f=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/CameraSharpness","w")
        f.write(str(CameraSharpness))
        
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        self.geometry('480x320')

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
    
    def exit(self,frame_class):
        GPIO.cleanup()
        os.popen("sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Shutdown.py")
        app.destroy()

    def quit_button_pressed(self,channel):
        GPIO.cleanup()
        os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Shutdown.py')
        app.destroy()
        quit()
    
    def SpeechSelector(self,frame_class):
        GPIO.cleanup()
        os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/S2B_Selector.py')
        app.destroy()
        
    def ImageSelector(self,frame_class):
        GPIO.cleanup()
        os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/I2B_Selector.py')
        app.destroy()
    
    def DigitalText(self,frame_class):
        GPIO.cleanup()
        time.sleep(1)
        os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/TextSelector.py')
        app.destroy()
        
    def TypeSelector(self, frame_class):
        GPIO.cleanup()
        os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/T2B_Selector.py')
        app.destroy()
        
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Select Mode:", font=("bold",15),height = 2) .pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Speech to Braille",font=("bold",10), height = 1, width = 60, bg='#fcd9d9', activebackground='CadetBlue1',
                  command=lambda: app.SpeechSelector(1)).pack()
        tk.Button(self, text="Image to Braille", font=("bold",10), height = 1, width = 60, bg='#fdcccd', activebackground='CadetBlue1',
                  command=lambda: app.ImageSelector(1)).pack()
        tk.Button(self, text="Digital Text Input", height = 1, width = 60, bg='#fdc0c2', activebackground='CadetBlue1',
                  command=lambda: app.DigitalText(1)).pack()
        tk.Button(self, text="Type Inputs", height = 1, width = 60, bg='#fdc0c2', activebackground='CadetBlue1',
                  command=lambda: app.TypeSelector(1)).pack()
        tk.Button(self, text="Settings", height = 1, width = 60, bg='#fdc0c2', activebackground='CadetBlue1',
                  command=lambda: master.switch_frame(Settings)).pack()
        tk.Button(self, text="Shutdown", height = 1, width = 60, bg='#f9a4a6', activebackground='CadetBlue1',
                  command=lambda: app.exit(1)).pack()

class Settings(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Settings", height = 2, width = 50, font=("bold")).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Braille Mode", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: master.switch_frame(BrailleModeFrame)).pack()
        tk.Button(self, text="Braille Speed", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: master.switch_frame(BrailleSpeedFrame)).pack()
        tk.Button(self, text="Number of Cells", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: master.switch_frame(BrailleCellFrame)).pack()
        tk.Button(self, text="Camera Config", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: master.switch_frame(CameraSettings)).pack()
        tk.Button(self, text="Return to start page", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: master.switch_frame(StartPage)).pack()

class SpeechAudio(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Press button 1 to select microphone as input, press button 2 to select audio file as input...", height = 2, width = 50, font=("bold")).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Live speech to Braille", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: master.switch_frame(CameraSettings)).pack()
        tk.Button(self, text="Audio File to Braille", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: master.switch_frame(StartPage)).pack()

class BrailleModeFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="BrailleMode", height = 3, width = 50, font=("bold")).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Automatic", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: [app.AutoMode(),master.switch_frame(auto)]).pack()
        tk.Button(self, text="Manual", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: [app.ManualMode(),master.switch_frame(manual)]).pack()
        tk.Button(self, text="Back to Settings", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: master.switch_frame(Settings)).pack()

class auto(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Automatic Mode Selected", height = 5, width = 50, bg='light pink', font=("bold")).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Back to Settings", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: master.switch_frame(Settings)).pack()

class manual(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Manual Mode Selected", height = 5, width = 50, bg='light pink', font=("bold")).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Back to Settings", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: master.switch_frame(Settings)).pack()

class BrailleSpeedFrame(tk.Frame):
    def __init__(self, master):
        global BrailleSpeed
        with open ("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/BrailleSpeed", "r") as text_file:
            BrailleSpeed=int(text_file.read())
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Braille Speed", height = 3, width = 50, font=("bold")).pack(side="top", fill="x", pady=10)
        tk.Label(self, text=(str(BrailleSpeed) + "second/s"), height = 3, width = 50, bg='light pink', font=("bold")).pack(side="top", fill="x", pady=10)        
        tk.Button(self, text="Increase", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: [app.BSpeedIncrease(),master.switch_frame(BrailleSpeedFrame)]).pack()
        tk.Button(self, text="Decrease", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: [app.BSpeedDecrease(),master.switch_frame(BrailleSpeedFrame)]).pack()
        tk.Button(self, text="Back to Settings", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: master.switch_frame(Settings)).pack()

class BrailleCellFrame(tk.Frame):
    def __init__(self, master):
        global numberofCells
        with open ("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/NumberOfCells", "r") as text_file:
            numberofCells=int(text_file.read())
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Number of Cells", height = 3, width = 50, font=("bold")).pack(side="top", fill="x", pady=10)
        tk.Label(self, text=(str(numberofCells)+ "cell/s"), height = 3, width = 50, bg='light pink', font=("bold")).pack(side="top", fill="x", pady=10)        
        tk.Button(self, text="Increase", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: [app.BCellIncrease(),master.switch_frame(BrailleCellFrame)]).pack()
        tk.Button(self, text="Decrease", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: [app.BCellDecrease(),master.switch_frame(BrailleCellFrame)]).pack()
        tk.Button(self, text="Back to Settings", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: master.switch_frame(Settings)).pack()

class CameraSettings(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Camera Settings", height = 3, width = 50, bg='light pink', font=("bold")).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Brightness", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: master.switch_frame(CameraBrightnessFrame)).pack()
        tk.Button(self, text="Saturation", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: master.switch_frame(CameraSaturationFrame)).pack()
        tk.Button(self, text="Sharpness", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: master.switch_frame(CameraSharpnessFrame)).pack()
        tk.Button(self, text="Back to Settings", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: master.switch_frame(Settings)).pack()

class CameraBrightnessFrame(tk.Frame):
    def __init__(self, master):
        global CameraBrightness
        with open ("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/CameraBrightness", "r") as text_file:
            CameraBrightness=int(text_file.read())
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Camera Brightness", height = 3, width = 50, font=("bold")).pack(side="top", fill="x", pady=10)
        tk.Label(self, text=str(CameraBrightness), height = 3, width = 50, bg='light pink', font=("bold")).pack(side="top", fill="x", pady=10)        
        tk.Button(self, text="Increase", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: [app.CameraBrightnessIncrease(),master.switch_frame(CameraBrightnessFrame)]).pack()
        tk.Button(self, text="Decrease", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: [app.CameraBrightnessDecrease(),master.switch_frame(CameraBrightnessFrame)]).pack()
        tk.Button(self, text="Back to Settings", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: master.switch_frame(Settings)).pack()

class CameraSaturationFrame(tk.Frame):
    def __init__(self, master):
        global CameraSaturation
        with open ("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/CameraSaturation", "r") as text_file:
            CameraSaturation=int(text_file.read())
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Camera Saturation", height = 3, width = 50, font=("bold")).pack(side="top", fill="x", pady=10)
        tk.Label(self, text=str(CameraSaturation), height = 3, width = 50, bg='light pink', font=("bold")).pack(side="top", fill="x", pady=10)        
        tk.Button(self, text="Increase", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: [app.CameraSaturationIncrease(),master.switch_frame(CameraSaturationFrame)]).pack()
        tk.Button(self, text="Decrease", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: [app.CameraSaturationDecrease(),master.switch_frame(CameraSaturationFrame)]).pack()
        tk.Button(self, text="Back to Settings", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: master.switch_frame(Settings)).pack()

class CameraSharpnessFrame(tk.Frame):
    def __init__(self, master):
        global CameraSharpness
        with open ("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/CameraSharpness", "r") as text_file:
            CameraSharpness=int(text_file.read())
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Camera Sharpness", height = 3, width = 50, font=("bold")).pack(side="top", fill="x", pady=10)
        tk.Label(self, text=str(CameraSharpness), height = 3, width = 50, bg='light pink', font=("bold")).pack(side="top", fill="x", pady=10)        
        tk.Button(self, text="Increase", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: [app.CameraSharpnessIncrease(),master.switch_frame(CameraSharpnessFrame)]).pack()
        tk.Button(self, text="Decrease", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: [app.CameraSharpnessDecrease(),master.switch_frame(CameraSharpnessFrame)]).pack()
        tk.Button(self, text="Back to Settings", height = 2, width = 20, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: master.switch_frame(Settings)).pack()
 
if __name__ == "__main__":
    app = MIMOBraille()
    app.title("MIMOBraille")
    app.setup()
    app.mainloop()
