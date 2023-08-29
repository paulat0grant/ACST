import os

print ("\nSTEP SIX OF LOGICAL PROCESSOR\n")
print ("METHOD-6: OPERATION STEREOISOMERS SYMBOL CHECK\n")

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
print ("REVERSE SMILES NOTATION FOR THE COMPOUNDS CHEMICAL STRUCTURE")
print (STRING1)
LEN1 = len(STRING1)
print ("NUMBER OF CHARACTER IN YOUR FILE: ")
print(LEN1)

ARRAY1 = list(STRING1)
#print (ARRAY1)

def swapHC(a, b):
    c = a
    a = b
    b = c
    return a, b


def SwapPost(arr):
    i = 0
    j = len(arr)
    while i < j-1:
                if arr[i] == '@':
                    if arr[i + 1]== '@':
                        if arr[i - 1] == 'H':
                            arr[i-1],arr[i+2] = swapHC(arr[i-1], arr[i+2])
                            i = i + 3
                        else:
                            arr[i], arr[i+2] = swapHC(arr[i], arr[i+2])
                            i = i + 3
                    else:
                        if arr[i - 1] == 'H':
                            arr[i-1],arr[i+1] = swapHC(arr[i-1], arr[i+1])
                            i = i + 2
                        else:
                            arr[i], arr[i+1] = swapHC(arr[i], arr[i+1])
                            i = i + 2
                else:
                    i = i + 1
                
SwapPost(ARRAY1)

STRING2 = ''.join(str(x) for x in ARRAY1)

print ("AFTER STEREOISOMER SYMBOL CORRECTION, REVERSE SMILES NOTATION BECOME: ")
print(STRING2)

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
    f.write(STRING2)

print("OPERATION STEREOISOMER SYMBOLISM PERFORMED SUCCESSFULLY")



