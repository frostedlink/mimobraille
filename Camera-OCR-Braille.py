import cv2 
import pytesseract
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import os
import RPi.GPIO as GPIO
import tkinter as tk
from tkinter import *

with open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/CameraBrightness", "r") as text_file:
    Brightness=text_file.read()
with open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/CameraSaturation", "r") as text_file:
    Saturation=text_file.read()
with open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/CameraSharpness", "r") as text_file:
    Sharpness=text_file.read()

class MIMOBraille(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(OCR)
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
    
    def closer(self):
        closer=0
        while closer==0:
            time.sleep(1)
            check=open("/home/MIMOBraille/Desktop/MIMOBraille/output.txt", "r", encoding="utf-8-sig")
            if check.read()=="":
                app.destroy()
                closer=1
    
    def main(self,frame_class):
        global Brightness
        global Saturation
        global Sharpness

        camera = PiCamera()
        camera.resolution = (480,320)
        camera.color_effects = (128,128)
        camera.brightness = int(Brightness)
        camera.framerate = 30
        camera.saturation= int(Saturation)
        camera.vflip=True
        camera.hflip=True
        camera.sharpness= int(Sharpness)

        rawCapture = PiRGBArray(camera, size=(480, 320)) 
        
        for frame in camera.capture_continuous(rawCapture, format="rgb", use_video_port=True):
            image = frame.array
            cv2.imshow("Image to Braille", image)
            key = cv2.waitKey(1) & 0xFF
            rawCapture.truncate(0)
            
            if GPIO.input(19):
                key=115

            if key == 115:
                text = pytesseract.image_to_string(image, config='-l eng --psm 1')
#                 print(text)
                f=open("/home/MIMOBraille/Desktop/MIMOBraille/output.txt", "w")
                f.write(text)
                cv2.imshow("Image to Braille", image)
                cv2.waitKey(1)
                cv2.destroyAllWindows()
#                 tk.Label(self, text="You said: " + text, height = 10, width = 45, bg='light pink', font=("bold",10),wraplength=480).pack(side="top", fill="x", pady=10)
                f.close()
                twidget=tk.Text(self,height = 10, width = 45)
                sbar=tk.Scrollbar(self)
                sbar.pack(side=tk.RIGHT)
                twidget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
                twidget.insert(tk.END,text)
                os.popen("sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Distributor.py")
                break
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        app.closer()
        
class OCR(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Press Button 1 to turn on Camera", height = 1, width = 45, font=("bold")).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Turn on Camera", height = 1, width = 60, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: app.main(1)).pack()
        tk.Button(self, text="Return to OCR input selection", height = 1, width = 60, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: app.quit_button_pressed(1)).pack()

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(12,GPIO.RISING,callback=app.main,bouncetime=200)
    GPIO.add_event_detect(13,GPIO.RISING,callback=app.quit_button_pressed,bouncetime=200)
    
    
if __name__ == "__main__":
    app = MIMOBraille()
    setup()
    app.mainloop()