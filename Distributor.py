import time
import os
import sys
import RPi.GPIO as GPIO
import serial

with open("/home/MIMOBraille/Desktop/MIMOBraille/Config Files/NumberOfCells", "r") as text_file:
    CellConfig=text_file.read()
  
#Replace with number of cells
numberOfCells = int(CellConfig)

with open("/home/MIMOBraille/Desktop/MIMOBraille/output.txt", "r") as text_file:
    text = text_file.read()
wordInput = text
wordSplit = list(wordInput)

AddChar=numberOfCells-((len(wordSplit)%numberOfCells))
adjustedLen=AddChar+(len(wordSplit))

wordIndexOverall1 = 0
wordIndexOverall2 = 0
wordIndexOverall3 = 0
wordIndexOverall4 = 0
wordIndexOverall5 = 0
wordIndexOverall6 = 0

word1letter = " "
word2letter = " "
word3letter = " "
word4letter = " "
word5letter = " "
word6letter = " "

GPIO.setmode(GPIO.BCM)
GPIO.setup(6,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

numericOn = 0
letterOn = 0
i=0

def serinit():
    if __name__ == "__main__":
        initext=numberOfCells
        ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
        ser.reset_input_buffer()
        ser.write(initext)
        time.sleep(1)
    time.sleep(.3)
    main()

def main():
    
    global i
    global numericOn
    global letterOn
    global AddChar
    
    while i < len(wordSplit): #Character checker
        if wordSplit[i].isupper() == True:
            wordSplit.insert(i, "$") #To make extra characters for uppercase sign
            i += 2
            
        elif wordSplit[i].isnumeric() == True:
            if numericOn == False:
                wordSplit.insert(i, "~") #To make extra characters for number sign
                numericOn = True
                i += 2
                
            elif numericOn == True:
                i += 1
                
        elif wordSplit[i].isnumeric() == False:
            if numericOn == True:
                wordSplit.insert(i, "^") #To make extra characters for letter sign
                letterOn = True
                numericOn = False
                i += 2
                
            elif letterOn == True:
                i += 1
                
            else:
                i += 1
    
    while AddChar>0:
        wordSplit.append(' ')
        AddChar=AddChar-1
    
    # Input code additional characters/append
    if numberOfCells == 1:
        global wordIndexOverall1
        if wordIndexOverall1<adjustedLen:
            global word1letter
            wordtoprint=""
            word1letter = (wordSplit[wordIndexOverall1])
            wordIndexOverall1 += 1 # Replace with number of cells
            print(word1letter)
            
            wordtoprint=word1letter
        else:
            clear=" "
            ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
            ser.reset_input_buffer()
            ser.write(clear.encode("utf8","ignore"))
            GPIO.cleanup()
            os.popen("sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Main-Program.py")
            sys.exit()
    
    if numberOfCells == 2:
        global wordIndexOverall2
        if wordIndexOverall2<adjustedLen:
            global word2letter
            wordtoprint=""
            word2letter = (wordSplit[wordIndexOverall2] + wordSplit[wordIndexOverall2+1])
            wordIndexOverall2 += 2 # Replace with number of cells
        
            wordtoprint=word2letter
            print(wordtoprint)
        else:
            clear="  "
            ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
            ser.reset_input_buffer()
            ser.write(clear.encode("utf8","ignore"))
            GPIO.cleanup()
            os.popen("sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Main-Program.py")
            sys.exit()

    if numberOfCells == 3:
        global wordIndexOverall3
        if wordIndexOverall3<adjustedLen:
            global word3letter
            wordtoprint=""
            word3letter = (wordSplit[wordIndexOverall3] + wordSplit[wordIndexOverall3+1] + wordSplit[wordIndexOverall3+2])
            wordIndexOverall3 += 3 # Replace with number of cells
        
            wordtoprint=word3letter
            print(wordtoprint)
        else:
            clear="   "
            ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
            ser.reset_input_buffer()
            ser.write(clear.encode("utf8","ignore"))
            GPIO.cleanup()
            os.popen("sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Main-Program.py")
            sys.exit()

    if numberOfCells == 4:
        global wordIndexOverall4
        if wordIndexOverall4<adjustedLen:
            global word4letter
            wordtoprint=""
            word4letter = "    "
            word4letter = (wordSplit[wordIndexOverall4] + wordSplit[wordIndexOverall4+1] + wordSplit[wordIndexOverall4+2] + wordSplit[wordIndexOverall4+3])
            wordIndexOverall4 += 4 # Replace with number of cells
            
            wordtoprint=word4letter
            print(wordtoprint)
        else:
            clear="    "
            ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
            ser.reset_input_buffer()
            ser.write(clear.encode("utf8","ignore"))
            GPIO.cleanup()
            os.popen("sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Main-Program.py")
            sys.exit()

    elif numberOfCells == 5:
        global wordIndexOverall5
        if wordIndexOverall5<adjustedLen:
            global word5letter
            wordtoprint=""
            word5letter = " "
            word5letter = (wordSplit[wordIndexOverall5] + wordSplit[wordIndexOverall5+1] + wordSplit[wordIndexOverall5+2] + wordSplit[wordIndexOverall5+3] + wordSplit[wordIndexOverall5+4])
            wordIndexOverall5 += 5 # Replace with number of cells
            
            wordtoprint=word5letter
            print(wordtoprint)
        else:
            clear="     "
            ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
            ser.reset_input_buffer()
            ser.write(clear.encode("utf8","ignore"))
            GPIO.cleanup()
            os.popen("sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Main-Program.py")
            sys.exit()

    elif numberOfCells == 6:
        global wordIndexOverall6
        if wordIndexOverall6<adjustedLen:
            global word6letter
            wordtoprint=""
            word6letter = " "
            word6letter = (wordSplit[wordIndexOverall6] + wordSplit[wordIndexOverall6+1] + wordSplit[wordIndexOverall6+2] + wordSplit[wordIndexOverall6+3] + wordSplit[wordIndexOverall6+4] + wordSplit[wordIndexOverall6+5] )
            wordIndexOverall6 += 6 # Replace with number of cells

            wordtoprint=word6letter
            print(wordtoprint)
        else:
            clear="      "
            ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
            ser.reset_input_buffer()
            ser.write(clear.encode("utf8","ignore"))
            GPIO.cleanup()
            os.popen("sudo python3 /home/MIMOBraille/Desktop/MIMOBraille/Main-Program.py")
            sys.exit()
            
    if __name__ == "__main__":
        ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
        ser.reset_input_buffer()
        ser.write(wordtoprint.encode("ascii","replace"))
        time.sleep(1)
        
    GPIO.wait_for_edge(6,GPIO.FALLING,bouncetime=200)
    main()
serinit()