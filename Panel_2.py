import sys
import os
from tkinter import *
from tkinter.ttk import Label

ACST=Tk()

ACST.title("ACST: LOGICAL PROCESSOR (LP) PANEL")
ACST.geometry('990x225')

#-----------------------------------------------------------------------------------------------------------------------------
Title1 = Label(ACST, text ="PANEL 2: LOGICAL PROCESSOR (LP)", font=("Arial 20 underline"))
Title1.grid(column=6, row=2)

#-----------------------------------------------------------------------------------------------------------------------------
StepOne = Label(ACST, text ="STEP", font=("Arial 14 underline"))
StepOne.grid(column=0, row=4)

StepOne = Label(ACST, text ="ONE", font=("Arial 14 underline"))
StepOne.grid(column=1, row=4)

StepOne = Label(ACST, text =":", font=("Arial 14"))
StepOne.grid(column=2, row=4)

StepOne = Label(ACST, text ="Reverse  String  Operation  on  SMILES  Notation  (click  'REVERSE  STRING' )", font=("Arial 14"))
StepOne.grid(column=6, row=4)

StepOne = Label(ACST, text =":", font=("Arial 14 "))
StepOne.grid(column=8, row=4)

def Step1():
    os.system('Step1.py')

ReversingString = Button(ACST, text="          REVERSE     STRING         ", bg="pink", fg="black",command=Step1)
ReversingString.grid(column=10, row=4)

#-----------------------------------------------------------------------------------------------------------------------------
StepTwo = Label(ACST, text ="STEP", font=("Arial 14 underline"))
StepTwo.grid(column=0, row=6)

StepTwo = Label(ACST, text ="TWO", font=("Arial 14 underline"))
StepTwo.grid(column=1, row=6)

StepTwo = Label(ACST, text =":", font=("Arial 14"))
StepTwo.grid(column=2, row=6)

StepTwo = Label(ACST, text ="Operation   Parenthesis   Regulation   (click  'PARENTHESIS   REGULATION' )", font=("Arial 14"))
StepTwo.grid(column=6, row=6)

StepTwo = Label(ACST, text =":", font=("Arial 14 "))
StepTwo.grid(column=8, row=6)

def Step2():
    os.system('Step2.py')

CorrParenthesis = Button(ACST, text=" PARENTHESIS   REGULATION ", bg="pink", fg="black",command=Step2)
CorrParenthesis.grid(column=10, row=6)

#-----------------------------------------------------------------------------------------------------------------------------
StepThree = Label(ACST, text ="STEP", font=("Arial 14 underline"))
StepThree.grid(column=0, row=8)

StepThree = Label(ACST, text ="THREE", font=("Arial 14 underline"))
StepThree.grid(column=1, row=8)

StepThree = Label(ACST, text =":", font=("Arial 14"))
StepThree.grid(column=2, row=8)

StepThree = Label(ACST, text ="Operation   Ring   Digits   Repositioning   ( click  'DIGIT  REPOSITIONING' )", font=("Arial 14"))
StepThree.grid(column=6, row=8)

StepThree = Label(ACST, text =":", font=("Arial 14 "))
StepThree.grid(column=8, row=8)

def Step3():
    os.system('Step3.py')

DigitReposition = Button(ACST, text="     DIGIT     REPOSITIONING     ", bg="pink", fg="black",command=Step3)
DigitReposition.grid(column=10, row=8)

#-----------------------------------------------------------------------------------------------------------------------------
StepFour = Label(ACST, text ="STEP", font=("Arial 14 underline"))
StepFour.grid(column=0, row=10)

StepFour = Label(ACST, text ="FOUR", font=("Arial 14 underline"))
StepFour.grid(column=1, row=10)

StepFour = Label(ACST, text =":", font=("Arial 14"))
StepFour.grid(column=2, row=10)

StepFour = Label(ACST, text ="Operation   Element   Symbol   Correction   (click   'SYMBOL   CORRECTION' )", font=("Arial 14"))
StepFour.grid(column=6, row=10)

StepFour = Label(ACST, text =":", font=("Arial 14 "))
StepFour.grid(column=8, row=10)

def Step4():
    os.system('Step4.py')

ElementCorrection = Button(ACST, text="     SYMBOL   CORRECTION     ", bg="pink", fg="black",command=Step4)
ElementCorrection.grid(column=10, row=10)

#-----------------------------------------------------------------------------------------------------------------------------
StepFive = Label(ACST, text ="STEP", font=("Arial 14 underline"))
StepFive.grid(column=0, row=12)

StepFive = Label(ACST, text ="FIVE", font=("Arial 14 underline"))
StepFive.grid(column=1, row=12)

StepFive = Label(ACST, text =":", font=("Arial 14"))
StepFive.grid(column=2, row=12)

StepFive = Label(ACST, text ="Operation  Ionic  Charge  Repositioning  (click 'CHARGE  REPOSITIONING' )", font=("Arial 14"))
StepFive.grid(column=6, row=12)

StepFive = Label(ACST, text =":", font=("Arial 14 "))
StepFive.grid(column=8, row=12)

def Step5():
    os.system('Step5.py')

ChargeCorrection = Button(ACST, text="    CHARGE  REPOSITIONING   ", bg="pink", fg="black",command=Step5)
ChargeCorrection.grid(column=10, row=12)

#-----------------------------------------------------------------------------------------------------------------------------
StepSix = Label(ACST, text ="STEP", font=("Arial 14 underline"))
StepSix.grid(column=0, row=14)

StepSix = Label(ACST, text ="SIX", font=("Arial 14 underline"))
StepSix.grid(column=1, row=14)

StepSix = Label(ACST, text =":", font=("Arial 14"))
StepSix.grid(column=2, row=14)

StepSix = Label(ACST, text ="Operation  Stereoisomer  Symbol  Check   (click 'CHECK STEREOISOMERS')", font=("Arial 14"))
StepSix.grid(column=6, row=14)

StepSix = Label(ACST, text =":", font=("Arial 14 "))
StepSix.grid(column=8, row=14)

def Step6():
    os.system('Step6.py')

StereoCorrection = Button(ACST, text="    CHECK  STEREOISOMERS    ", bg="pink", fg="black",command=Step6)
StereoCorrection.grid(column=10, row=14)

#-----------------------------------------------------------------------------------------------------------------------------
DivisionExit = Label(ACST, text ="EXIT", font=("Arial 14 underline"))
DivisionExit.grid(column=0, row=16)

DivisionExit = Label(ACST, text ="PANEL", font=("Arial 14 underline"))
DivisionExit.grid(column=1, row=16)

DivisionExit = Label(ACST, text =":", font=("Arial 14"))
DivisionExit.grid(column=2, row=16)

DivisionExit = Label(ACST, text ="Click 'EXIT-PANEL' to Exit from the LP Division (click 'EXIT-PANEL' )", font=("Arial 14"))
DivisionExit.grid(column=6, row=16)

DivisionExit = Label(ACST, text =":", font=("Arial 14 "))
DivisionExit.grid(column=8, row=16)

DivisionExit = Button(ACST, text=" EXIT - PANEL ",font=("Arial 10"), bg="blue", fg="white", command=ACST.destroy)
DivisionExit.grid(column=10, row=16)


#-----------------------------------------------------------------------------------------------------------------------------
ACST.mainloop()
