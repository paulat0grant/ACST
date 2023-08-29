import sys
import os
from tkinter import *
from tkinter.ttk import Label

ACST=Tk()

ACST.title("ACST: Home Page")
ACST.geometry('1300x180')

#-----------------------------------------------------------------------------------------------------------------------------
TitleLine1 = Label(ACST, text =" ASCII Text based Chemical Structure Tuner (ACST)  :", font=("Arial 20 underline"))
TitleLine1.grid(column=3, row=2)

TitleLine2 = Label(ACST, text =" Reverse String Mechanism for SMILES Notation ", font=("Arial 20 underline"))
TitleLine2.grid(column=3, row=3)

#-----------------------------------------------------------------------------------------------------------------------------

Module1 = Label(ACST, text ="              USER  MANUAL              :", font=("Arial 14 underline"))
Module1.grid(column=0, row=4)

Module1 = Label(ACST, text ="Read 'USER MANUAL' for Help & Instructions to use Chemical Structure Tuner (ACST) (click 'MANUAL')", font=("Arial 14"))
Module1.grid(column=3, row=4) 

Module1 = Label(ACST, text =":", font=("Arial 14 "))
Module1.grid(column=8, row=4)

def UserManual():
    os.system('User_Manual.pdf')

Manual = Button(ACST, text="  M A N U A L  ", bg="pink", fg="black",command=UserManual)
Manual.grid(column=10, row=4)

#-----------------------------------------------------------------------------------------------------------------------------
Module2 = Label(ACST, text ="CHEMICAL FILE TRANSLATOR:", font=("Arial 14 underline"))
Module2.grid(column=0, row=6)

Module2 = Label(ACST, text ="Launch 'CHEMICAL FILE TRANSLATOR' to Draw, Convert and Edit Chemical Files (click 'TRANSLATOR')", font=("Arial 14"))
Module2.grid(column=3, row=6)

Module2 = Label(ACST, text =":", font=("Arial 14 "))
Module2.grid(column=8, row=6)

def Panel_1():
    os.system('Panel_1.py')

Translator = Button(ACST, text=" TRANSLATOR ", bg="pink", fg="black",command=Panel_1)
Translator.grid(column=10, row=6)

#-----------------------------------------------------------------------------------------------------------------------------
Module3 = Label(ACST, text ="      LOGICAL  PROCESSOR      :", font=("Arial 14 underline"))
Module3.grid(column=0, row=8)

Module3 = Label(ACST, text ="Launch  'LOGICAL PROCESSOR'  for  String  Reversal Steps on SMILES  Notation (click 'PROCESSOR' )", font=("Arial 14"))
Module3.grid(column=3, row=8)

Module3 = Label(ACST, text =":", font=("Arial 14 "))
Module3.grid(column=8, row=8)

def Panel_2():
    os.system('Panel_2.py')

Processor = Button(ACST, text="   PROCESSOR  ", bg="pink", fg="black",command=Panel_2)
Processor.grid(column=10, row=8)

#-----------------------------------------------------------------------------------------------------------------------------
Module4 = Label(ACST, text ="           S H U T  -  D O W N           :", font=("Arial 14 underline"))
Module4.grid(column=0, row=10)

Module4 = Label(ACST, text ="Click 'SHUT-DOWN' to Exit the Application (click   'SHUT-DOWN' )", font=("Arial 14"))
Module4.grid(column=3, row=10)

Module4 = Label(ACST, text =":", font=("Arial 14 "))
Module4.grid(column=8, row=10)

Exit = Button(ACST, text="SHUT-DOWN",font=("Arial 10"), bg="blue", fg="white", command=ACST.destroy)
Exit.grid(column=10, row=10)

#-----------------------------------------------------------------------------------------------------------------------------

ACST.mainloop()
