#-----------------------------------Tkinter------------------------------------#
import sys
from tkinter import *

#-----------------------------------Submit-------------------------------------#
def Submit():
    print("Submit")

#------------------------------------Exit--------------------------------------#
def Exit(): 
  myWindow.destroy()

#--------------------------Areyousureexitfunction------------------------------#
def EndFunction ():
    messagebox.askokcancel("Are you sure you want to quit?",
                           "Are you sure you want to quit?")
    if messagebox.askokcancel() == True:
        quit()

#------------------------------WindowPreferences-------------------------------#
myWindow = Tk()
myWindowtitle = myWindow.title("AQA Logic Puzzle")
myWindow.configure(background= "#F7F7F7")
myWindow.minsize(500,300)

#-----------------------------------OpenWordFile-------------------------------#
def openFile():
    global words

    words = []
    with open ("words.txt", "r") as codedWords:
        for line in codedWords:
            words.append(line.rstrip("\n"))
        print(words)
    Check()

#------------------------------Labelcolumntitle----------------------------#
labeltitle = Label(myWindow, text="AQA Logic Puzzle", font=("Helvetica", 15))
labeltitle.grid(row = 0, column = 6)
labeltitle.configure(background= "#F7F7F7")

#------------------------------Labelcolumn1----------------------------#
#----This part of the code decides what the label is going to say------#
label2 = Label(myWindow, text = "!")
#---This part of the code decides where to put the label on the GUI----#
label2.grid(row = 3, column = 1)
#This part of the code decides what background colour of the label is--#
label2.configure(background= "#F7F7F7")

label3 = Label(myWindow, text = "+")
label3.grid(row = 4, column = 1)
label3.configure(background= "#F7F7F7")

label4 = Label(myWindow, text = "-")
label4.grid(row = 5, column = 1)
label4.configure(background= "#F7F7F7")

label5 = Label(myWindow, text = ":")
label5.grid(row = 6, column = 1)
label5.configure(background= "#F7F7F7")

label6 = Label(myWindow, text = "(")
label6.grid(row = 7, column = 1)
label6.configure(background= "#F7F7F7")

label7 = Label(myWindow, text = "/")
label7.grid(row = 8, column = 1)
label7.configure(background= "#F7F7F7")

label8 = Label(myWindow, text = ".")
label8.grid(row = 9, column = 1)
label8.configure(background= "#F7F7F7")

label9 = Label(myWindow, text = ' " ')
label9.grid(row = 10, column = 1)
label9.configure(background= "#F7F7F7")

label10 = Label(myWindow, text = ",")
label10.grid(row = 11, column = 1)
label10.configure(background= "#F7F7F7")

label11 = Label(myWindow, text = "$")
label11.grid(row = 12, column = 1)
label11.configure(background= "#F7F7F7")

label12 = Label(myWindow, text = "*")
label12.grid(row = 13, column = 1)
label12.configure(background= "#F7F7F7")

label13 = Label(myWindow, text = "%")
label13.grid(row = 14, column = 1)
label13.configure(background= "#F7F7F7")

label14 = Label(myWindow, text = ")")
label14.grid(row = 15, column = 1)
label14.configure(background= "#F7F7F7")

#------------------------------Labelcolumn2----------------------------#

label5 = Label(myWindow, text = "#")
label5.grid(row = 3, column = 6)
label5.configure(background= "#F7F7F7")

label6 = Label(myWindow, text = "&")
label6.grid(row = 4, column = 6)
label6.configure(background= "#F7F7F7")

label7 = Label(myWindow, text = "'")
label7.grid(row = 5, column = 6)
label7.configure(background= "#F7F7F7")

label8 = Label(myWindow, text = "0")
label8.grid(row = 6, column = 6)
label8.configure(background= "#F7F7F7")

label9 = Label(myWindow, text = "1")
label9.grid(row = 7, column = 6)
label9.configure(background= "#F7F7F7")

label20 = Label(myWindow, text = "2")
label20.grid(row = 8, column = 6)
label20.configure(background= "#F7F7F7")

label21 = Label(myWindow, text = "3")
label21.grid(row = 9, column = 6)
label21.configure(background= "#F7F7F7")

label22 = Label(myWindow, text = "4")
label22.grid(row = 10, column = 6)
label22.configure(background= "#F7F7F7")

label23 = Label(myWindow, text = "5")
label23.grid(row = 11, column = 6)
label23.configure(background= "#F7F7F7")

label24 = Label(myWindow, text = "6")
label24.grid(row = 12, column = 6)
label24.configure(background= "#F7F7F7")

label25 = Label(myWindow, text = "7")
label25.grid(row = 13, column = 6)
label25.configure(background= "#F7F7F7")

label26 = Label(myWindow, text = "8")
label26.grid(row = 14, column = 6)
label26.configure(background= "#F7F7F7")

label27 = Label(myWindow, text = "9")
label27.grid(row = 15, column = 6)
label27.configure(background= "#F7F7F7")

#------------------------------------Copyright-----------------------------------#
#-------This Decides what a label says and the font and font size of it---------#
Copylabel = Label(myWindow, text="©Ellis Fossett 2014", font=("Helvetica", 8))
Copylabel.grid(row = 20, column = 6)
Copylabel.configure(background= "#F7F7F7")

#----------------------------------Buttons-----------------------------------#
buttonSubmit = Button(myWindow, text = "Check", command = openFile)
buttonSubmit.grid(row = 20, column = 1)
buttonSubmit.config(height = 1, width = 15)

buttonExit = Button(myWindow, text = "Exit", command = EndFunction)
buttonExit.grid(row = 20, column = 10)
buttonExit.config(height = 1, width = 15)

#--------------------EntryBoxColumn1--------------------#
#---------This decides the entrybox name as it will be important later--------#
Exclamation = Entry(myWindow)
Exclamation.grid(row = 3, column = 4)

Plus = Entry(myWindow)
Plus.grid(row = 4, column = 4)

Minus = Entry(myWindow)
Minus.grid(row = 5, column = 4)

Colon = Entry(myWindow)
Colon.grid(row = 6, column = 4)

BracketL = Entry(myWindow)
BracketL.grid(row = 7, column = 4)

Slash = Entry(myWindow)
Slash.grid(row = 8, column = 4)

Period = Entry(myWindow)
Period.grid(row = 9, column = 4)

Speach = Entry(myWindow)
Speach.grid(row = 10, column = 4)

Comma = Entry(myWindow)
Comma.grid(row = 11, column = 4)

Dollar = Entry(myWindow)
Dollar.grid(row = 12, column = 4)

Astrix = Entry(myWindow)
Astrix.grid(row = 13, column = 4)
Astrix.insert(0,"M")

Percent = Entry(myWindow)
Percent.grid(row = 14, column = 4)
Percent.insert(0,"N")

BracketR = Entry(myWindow)
BracketR.grid(row = 15, column = 4)


#-------------------EntryBoxColumn2----------------#

HashTag = Entry(myWindow)
HashTag.grid(row = 3, column = 8)
HashTag.insert(0,"A")

Anfersan = Entry(myWindow)
Anfersan.grid(row = 4, column = 8)

Apostrophe = Entry(myWindow)
Apostrophe.grid(row = 5, column = 8)

Zero = Entry(myWindow)
Zero.grid(row = 6, column = 8)

One = Entry(myWindow)
One.grid(row = 7, column = 8)
 
Two = Entry(myWindow)
Two.grid(row = 8, column = 8)

Three = Entry(myWindow)
Three.grid(row = 9, column = 8)

Four = Entry(myWindow)
Four.grid(row = 10, column = 8)

Five = Entry(myWindow)
Five.grid(row = 11, column = 8)

Six = Entry(myWindow)
Six.grid(row = 12, column = 8)

Seven = Entry(myWindow)
Seven.grid(row = 13, column = 8)

Eight = Entry(myWindow)
Eight.grid(row = 14, column = 8)

Nine = Entry(myWindow)
Nine.grid(row = 15, column = 8)

#-----------------------------------EntryBoxCheck-----------------------------------#
def Check():
    global words
    if Entry.get(Exclamation) != "":
        for x in range(len(words)):
            words[x] = words[x].replace("!",Entry.get(Exclamation))

    if Entry.get(Plus) != "":
        for x in range(len(words)):
            words[x] = words[x].replace("+",Entry.get(Plus))

    if Entry.get(Minus) != "":
        for x in range(len(words)):
            words[x] = words[x].replace("-",Entry.get(Minus))

    if Entry.get(Colon) != "":
        for x in range(len(words)):
            words[x] = words[x].replace(":",Entry.get(Colon))

    if Entry.get(BracketL) != "":
        for x in range(len(words)):
            words[x] = words[x].replace("(",Entry.get(BracketL))

    if Entry.get(Slash) != "":
        for x in range(len(words)):
            words[x] = words[x].replace(" / ",Entry.get(Slash))

    if Entry.get(Period) != "":
        for x in range(len(words)):
            words[x] = words[x].replace(".",Entry.get(Period))

    if Entry.get(Speach) != "":
        for x in range(len(words)):
            words[x] = words[x].replace('"',Entry.get(Speach))

    if Entry.get(Comma) != "":
        for x in range(len(words)):
            words[x] = words[x].replace(",",Entry.get(Comma))

    if Entry.get(Dollar) != "":
        for x in range(len(words)):
            words[x] = words[x].replace("$",Entry.get(Dollar))

    if Entry.get(Astrix) != "":
        for x in range(len(words)):
            words[x] = words[x].replace("*",Entry.get(Astrix))

    if Entry.get(Percent) != "":
        for x in range(len(words)):
            words[x] = words[x].replace("%",Entry.get(Percent))

    if Entry.get(BracketR) != "":
        for x in range(len(words)):
            words[x] = words[x].replace(")",Entry.get(BracketR))

    if Entry.get(HashTag) != "":
        for x in range(len(words)):
            words[x] = words[x].replace("#",Entry.get(HashTag))

    if Entry.get(Anfersan) != "":
        for x in range(len(words)):
            words[x] = words[x].replace("&",Entry.get(Anfersan))

    if Entry.get(Apostrophe) != "":
        for x in range(len(words)):
            words[x] = words[x].replace("'",Entry.get(Apostrophe))

    if Entry.get(Zero) != "":
        for x in range(len(words)):
            words[x] = words[x].replace("0",Entry.get(Zero))

    if Entry.get(One) != "":
        for x in range(len(words)):
            words[x] = words[x].replace("1",Entry.get(One))

    if Entry.get(Two) != "":
        for x in range(len(words)):
            words[x] = words[x].replace("2",Entry.get(Two))

    if Entry.get(Three) != "":
        for x in range(len(words)):
            words[x] = words[x].replace("3",Entry.get(Three))

    if Entry.get(Four) != "":
        for x in range(len(words)):
            words[x] = words[x].replace("4",Entry.get(Four))

    if Entry.get(Five) != "":
        for x in range(len(words)):
            words[x] = words[x].replace("5",Entry.get(Five))

    if Entry.get(Six) != "":
        for x in range(len(words)):
            words[x] = words[x].replace("6",Entry.get(Six))

    if Entry.get(Seven) != "":
        for x in range(len(words)):
            words[x] = words[x].replace("7",Entry.get(Seven))

    if Entry.get(Eight) != "":
        for x in range(len(words)):
            words[x] = words[x].replace("8",Entry.get(Eight))

    if Entry.get(Nine) != "":
        for x in range(len(words)):
            words[x] = words[x].replace("9",Entry.get(Nine))

    print(words)
