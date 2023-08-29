import os

print ("\nSTEP ONE OF LOGICAL PROCESSOR\n")
print ("METHOD-1: REVERSE STRING OPERATION\n")

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
STRING1 = f.read()
print ("THE SMILES NOTATION FOR THE COMPOUNDS CHEMICAL STRUCTURE")
print (STRING1)
LEN1 = len(STRING1)
print ("NUMBER OF CHARACTER IN YOUR FILE: ")
print(LEN1)


def ReverseString(c):
  return c[::-1]

STRING2 = ReverseString(STRING1)

print ("REVERSE OF ABOVE SMILES NOTATION: ")
print(STRING2)

ARRAY1 = list(STRING2)

ARRAY2 = ARRAY1.remove(ARRAY1[0])

STRING3 = ''.join(str(x) for x in ARRAY1)

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

print("STEP ONE: REVERSE STRING OPERATION SUCCESSFULLY PERFORMED")
