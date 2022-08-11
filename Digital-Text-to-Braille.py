import RPi.GPIO as GPIO
import tkinter as tk
import os
import docx2txt
import PyPDF4
import time
import shutil
from tkinter import *

class MIMOBraille(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(DigitalText)
        self.geometry('480x320')
    
    def distributor(self,frame_class):
        cell=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/BrailleMode")
        distribmode=int(cell.read())
        
        if distribmode==0:
            os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Distributor_Auto.py')
        
        elif distribmode==1:
            os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Distributor.py')

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()  

    def quit_button_pressed(self,channel):
        closer=1
        GPIO.cleanup()
        os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/TextSelector.py')
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
    
    def distributor(self,frame_class):
        cell=open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/BrailleMode")
        distribmode=int(cell.read())
        
        if distribmode==0:
            os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Distributor_Auto.py')
        
        elif distribmode==1:
            os.popen('sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Distributor.py')
    
    def file_man(self,frame_class):
        os.popen("orca")
        os.popen("sudo pcmanfm /media/MIMOBraille/")
        app.checker()
    
    def checker(self):
        if not os.listdir('/media/MIMOBraille/Digital-Text to Braille Output/'):
            time.sleep(1)
            app.checker()
        else:
            os.popen("sudo pkill pcmanfm")
            app.reader()
    
    def reader(self):
        for file in os.listdir("/media/MIMOBraille/Digital-Text to Braille Output/"):
            if file.endswith(".pdf"):
                new_name = r"/media/MIMOBraille/Digital-Text to Braille Output/output.pdf"
                os.rename(os.path.join("/media/MIMOBraille/Digital-Text to Braille Output/", file), new_name)
                pdfFileObj=open("/media/MIMOBraille/Digital-Text to Braille Output/output.pdf", "rb")
                pdfReader=PyPDF4.PdfFileReader(pdfFileObj)
                num_pages = pdfReader.getNumPages()
                page=0;
                text = ""
                while page < num_pages:
                    pageObj = pdfReader.getPage(page)
                    page = page+1
                    text += pageObj.extractText()
                    dtxt=open("/home/MIMOBraille/Desktop/MIMOBraille/output.txt","w")
                    dtxt.write(text)
                    dtxt.close()
                    clear()
            elif file.endswith(".docx"):
                new_name = r"/media/MIMOBraille/Digital-Text to Braille Output/output.docx"
                os.rename(os.path.join("/media/MIMOBraille/Digital-Text to Braille Output/", file), new_name)
                text = docx2txt.process("/media/MIMOBraille/Digital-Text to Braille Output/output.docx")
                dtxt=open("/home/MIMOBraille/Desktop/MIMOBraille/output.txt","w")
                dtxt.write(text)
                dtxt.close()
                clear()
            elif file.endswith(".txt"):
                new_name = r"/media/MIMOBraille/Digital-Text to Braille Output/output.txt"
                os.rename(os.path.join("/media/MIMOBraille/Digital-Text to Braille Output/", file), new_name)
                original = r"/media/MIMOBraille/Digital-Text to Braille Output/output.txt"
                target = r"/home/MIMOBraille/Desktop/MIMOBraille/output.txt"
                shutil.copyfile(original, target)
                clear()
            else:
                tk.Label(self, text="Invalid File Type",height = 3, width = 45, font=("bold",10),wraplength=480).pack(side="top", fill="x", pady=10)
                continue
            
            dtxt=open("/home/MIMOBraille/Desktop/MIMOBraille/output.txt","r",encoding="utf-8-sig")
            outputtext=dtxt.read()
            twidget=tk.Text(self,height = 10, width = 45)
            sbar=tk.Scrollbar(self)
            sbar.pack(side=tk.RIGHT)
            twidget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            twidget.insert(tk.END,outputtext)
            app.distributor(1)
            app.closer()

class DigitalText(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Press Button 1,to start browsing...", height = 1, width = 45, font=("bold")).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Browse for Document", height = 1, width = 60, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: app.file_man(1)).pack()
        tk.Button(self, text="Return to Digital text input selection", height = 1, width = 60, bg='light pink', activebackground='CadetBlue1',
                  command=lambda: app.quit_button_pressed(1)).pack()
        
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(12,GPIO.RISING,callback=app.file_man,bouncetime=200)
    GPIO.add_event_detect(13,GPIO.RISING,callback=app.quit_button_pressed,bouncetime=200)

def clear():
    for root, dirs, files in os.walk('/media/MIMOBraille/Digital-Text to Braille Output'):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))

if __name__ == "__main__":
    app = MIMOBraille()
    app.title("Digital Text to Braille")
    setup()
    clear()
    app.mainloop()

