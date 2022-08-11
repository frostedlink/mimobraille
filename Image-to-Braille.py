import pytesseract
import os
import shutil
import time
import RPi.GPIO as GPIO
import tkinter as tk
from tkinter import *
from pynput.keyboard import *
from PIL import Image

class MIMOBraille(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(ImageBraille)
        self.geometry('480x320')

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()  

    def quit_button_pressed(self,channel):
        GPIO.cleanup()
        os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/I2B_Selector.py')
        app.destroy()

    def file_man(self,frame_class):
        os.popen("orca")
        os.popen("sudo pcmanfm /media/MIMOBraille/")
        app.checker()
    
    def closer(self):
        closer=0
        while closer==0:
            time.sleep(1)
            check=open("/home/MIMOBraille/Desktop/MIMOBraille/output.txt", "r", encoding="utf-8-sig")
            if check.read()=="":
                app.destroy()
                closer=1
    
    def distributor(self,frame_class):
        cell=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/BrailleMode")
        distribmode=int(cell.read())
        
        if distribmode==0:
            os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Distributor_Auto.py')
        
        elif distribmode==1:
            os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Distributor.py')
    
    def checker(self):
        if not os.listdir('/media/MIMOBraille/Image to Braille Output'):
            time.sleep(1)
            app.checker()
        else:
            os.popen("sudo pkill pcmanfm")
            app.main(1)
    
    def main(self,frame_class):
        for file in os.listdir("/media/MIMOBraille/Image to Braille Output"):
            if file.endswith(".jpg"):
                new_name = r"/media/MIMOBraille/Image to Braille Output/output.jpg"
                os.rename(os.path.join("/media/MIMOBraille/Image to Braille Output/", file), new_name)
                img=Image.open("/media/MIMOBraille/Image to Braille Output/output.jpg")
                img.save("/media/MIMOBraille/Image to Braille Output/output.png")
                text = pytesseract.image_to_string("/media/MIMOBraille/Image to Braille Output/output.png", config='-l eng --psm 1')
                itxt=open("/home/MIMOBraille/Desktop/MIMOBraille/output.txt","w")
                itxt.write(text)
                itxt.close()
                clear()
            elif file.endswith(".png"):
                new_name = r"/media/MIMOBraille/Image to Braille Output/output.png"
                os.rename(os.path.join("/media/MIMOBraille/Image to Braille Output/", file), new_name)
                text = pytesseract.image_to_string("/media/MIMOBraille/Image to Braille Output/output.png", config='-l eng --psm 1')
                itxt=open("/home/MIMOBraille/Desktop/MIMOBraille/output.txt","w")
                itxt.write(text)
                itxt.close()
                clear()
            else:
                tk.Label(self, text="Invalid File Type",height = 3, width = 45, font=("bold",10),wraplength=480).pack(side="top", fill="x", pady=10)
                clear()
                continue
        
            itxt=open("/home/MIMOBraille/Desktop/MIMOBraille/output.txt", "r")
            outputtext=itxt.read()

            twidget=tk.Text(self,height = 10, width = 45)
            sbar=tk.Scrollbar(self)
            sbar.pack(side=tk.RIGHT)
            twidget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            twidget.insert(tk.END,outputtext)
            app.distributor(1)
            app.closer()
            
            
class ImageBraille(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Press Button 1 to Start Browsing", height = 1, width = 45, font=("bold")).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Browse for Image file", height = 1, width = 60, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: app.file_man(1)).pack()
        tk.Button(self, text="Return to OCR input selection", height = 1, width = 60, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: app.quit_button_pressed(1)).pack()

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(12,GPIO.RISING,callback=app.file_man,bouncetime=200)
    GPIO.add_event_detect(13,GPIO.RISING,callback=app.quit_button_pressed,bouncetime=200)

def clear():
    for root, dirs, files in os.walk('/media/MIMOBraille/Image to Braille Output'):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))

if __name__ == "__main__":
    app = MIMOBraille()
    app.title("Image file to Braille")
    setup()
    clear()
    app.mainloop()
