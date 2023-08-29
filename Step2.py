import os

print ("\nSTEP TWO OF LOGICAL PROCESSOR\n")
print ("METHOD-2: OPERATION PARENTHESIS REGULATION\n")
print ("\nYOUR CURRENT DIRECTORY: ")
print (os.getcwd()+ "\n")

ANS01 = 'NO'
while ANS01 != 'YES' :
    DIR1 = input("ENTER DIRECTORY OF THE FILE: \n")
    ANS01 = input("YOUR FILE IS THE DIRECTORY: "+ DIR1 + "\nYES or NO: ")
    print ('YOU HAVE ENTERED:' + ANS01)

os.chdir(DIR1)
print ("NOW, YOUR CURRENT DIRECTORY: ")
print (os.getcwd()+ "\n")

ANS02 = 'NO'
while ANS02 != 'YES' :
    FILE1 = input("ENTER NAME OF THE FILE: \n")

    ANS02 = input("YOUR FILE NAME IS: "+ FILE1 + "\nYES or NO: ")
    print ('YOU HAVE ENTERED:' + ANS02)

f = open(FILE1, 'r')
STRING2 = f.read()
print ("THE SMILES NOTATION FOR THE COMPOUNDS CHEMICAL STRUCTURE")
print (STRING2)
LEN1 = len(STRING2)
print ("NUMBER OF CHARACTER IN YOUR FILE: ")
print(LEN1)


FindPeren1 = '['
ReplPeren1 = ']'

FindPeren2 = ']'
ReplPeren2 = '['

FindPeren3 = '('
ReplPeren3 = ')'

FindPeren4 = ')'
ReplPeren4 = '('

STRING3 = ''

for elem in STRING2:
    if elem == FindPeren1:
        STRING3 += ReplPeren1
    elif elem == FindPeren2:
        STRING3 += ReplPeren2
    elif elem == FindPeren3:
         STRING3 += ReplPeren3
    elif elem == FindPeren4:
         STRING3 += ReplPeren4
    else:
         STRING3 += elem

print ("AFTER PERENTHESIS CORRECTION, REVERSE SMILES NOTATION BECOME: ")
print (STRING3)


ANS03 = 'NO'
while ANS03 != 'YES':
    DIR2 = input("ENTER DIRECTORY TO SAVE THE FILE: \n")
    ANS03 = input("YOUR THE DIRECTORY WILL BE: " + DIR2 + "\nYES or NO: ")
    print('YOU HAVE ENTERED:' + ANS03)

os.chdir(DIR2)
print("NOW, YOUR CURRENT DIRECTORY: ")
print(os.getcwd() + "\n")

ANS04 = 'NO'
while ANS04 != 'YES':
    FILE2 = input("ENTER NAME OF THE FILE (as 'xyz.smiles'): \n")
    ANS04 = input("YOUR FILE NAME IS: " + FILE2 + "\nYES or NO: ")
    print('YOU HAVE ENTERED:' + ANS04)

with open(FILE2, mode='w', newline='') as f:
    f.write(STRING3)

print("STEP TWO: OPERATION PARENTHESIS REGULATION SUCCESSFULLY PERFORMED")
