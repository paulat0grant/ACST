import sys
import os
from tkinter import *
from tkinter.ttk import Label

ACST=Tk()

ACST.title("ACST: CHEMICAL FILE TRANSLATOR (CFT) PANEL")
ACST.geometry('1056x150')

#-----------------------------------------------------------------------------------------------------------------------------
Title1 = Label(ACST, text ="PANEL 1: CHEMICAL FILES TRANSLATOR (CFT)", font=("Arial 20 underline"))
Title1.grid(column=3, row=2)

#-----------------------------------------------------------------------------------------------------------------------------

Software1 = Label(ACST, text ="    DRAWING   SOFTWARE  :", font=("Arial 14 underline"))
Software1.grid(column=0, row=4)

Software1 = Label(ACST, text ="Draw   Molecular   Structure   of   the   Compound  ( click 'DRAW MOLECULE' )", font=("Arial 14"))
Software1.grid(column=3, row=4)

Software1 = Label(ACST, text =":", font=("Arial 14 "))
Software1.grid(column=8, row=4)

def DrawMolecule():
    os.system('Panel_1DrawMolecule.py')

Software1 = Button(ACST, text=" DRAW MOLECULE ", bg="pink", fg="black",command=DrawMolecule)
Software1.grid(column=10, row=4)

#-----------------------------------------------------------------------------------------------------------------------------
Software2 = Label(ACST, text ="TRANSLATING SOFTWARE:", font=("Arial 14 underline"))
Software2.grid(column=0, row=6)

Software2 = Label(ACST, text ="Molecule Structure/SMILES Notation Conversion (click 'FILE TRANSLATION' )", font=("Arial 14"))
Software2.grid(column=3, row=6)

Software2 = Label(ACST, text =":", font=("Arial 14 "))
Software2.grid(column=8, row=6)

def FileTranslate():
    os.system('Panel_1FileTranslate.py')

Software2 = Button(ACST, text="FILE TRANSLATION", bg="pink", fg="black",command=FileTranslate)
Software2.grid(column=10, row=6)

#-----------------------------------------------------------------------------------------------------------------------------
Software3 = Label(ACST, text ="TEXT-EDITING SOFTWARE:", font=("Arial 14 underline"))
Software3.grid(column=0, row=8)

Software3 = Label(ACST, text ="Display/Edit the SMILES Notation String on Text-Editor(click 'TEXT-EDITING' )", font=("Arial 14"))
Software3.grid(column=3, row=8)

Software3 = Label(ACST, text =":", font=("Arial 14 "))
Software3.grid(column=8, row=8)

def TextEditor():
    os.system('Panel_1TextEditor.py')

Software3 = Button(ACST, text="     TEXT - EDITING   ", bg="pink", fg="black",command=TextEditor)
Software3.grid(column=10, row=8)
#-----------------------------------------------------------------------------------------------------------------------------
DivisionExit = Label(ACST, text ="       E X I T  -  P A N E L         :", font=("Arial 14 underline"))
DivisionExit.grid(column=0, row=10)

DivisionExit = Label(ACST, text ="Click 'EXIT-PANEL' to Exit from the CFT Division (click 'EXIT-PANEL' )", font=("Arial 14"))
DivisionExit.grid(column=3, row=10)

DivisionExit = Label(ACST, text =":", font=("Arial 14 "))
DivisionExit.grid(column=8, row=10)

DivisionExit = Button(ACST, text=" EXIT - PANEL ",font=("Arial 10"), bg="blue", fg="white", command=ACST.destroy)
DivisionExit.grid(column=10, row=10)


#-----------------------------------------------------------------------------------------------------------------------------
ACST.mainloop()
