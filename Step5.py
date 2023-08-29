import os

print ("\nSTEP FIVE OF LOGICAL PROCESSOR\n")
print ("METHOD-5: OPERATION IONIC CHARGE REPOSITIONING\n")

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


def swapFour(a, b, c, d):
    e = a
    a = c
    c = b
    b = d
    d = e
    return a, b, c, d

def swapThree(a, b, c):
    d = a
    a = c
    c = d
    return a, b, c

def swap0Three(a, b, c):
    e = a
    a = b
    b = c
    c = e
    return a, b, c

def swap0Two(a, b):
    c = a
    a = b
    b = c
    return a, b

def SwapPost(arr):
    i = 0
    j = len(arr)
    while i < j-1:
                if arr[i] == '-' or arr[i] == '+':
                    if arr[i - 1].isdigit():
                        if arr[i + 3] == ']':
                            arr[i-1], arr[i], arr[i+1], arr[i+2] = swapFour(arr[i-1],arr[i], arr[i+1], arr[i+2])
                            i = i + 3
                        else:
                            arr[i-1], arr[i], arr[i+1] = swapThree(arr[i-1],arr[i], arr[i+1])
                            i = i + 2
                    else:
                        if arr[i + 3] == ']':
                            arr[i], arr[i+1], arr[i+2] = swap0Three(arr[i], arr[i+1], arr[i+2])
                            i = i + 3
                        else:
                            arr[i], arr[i+1] = swap0Two(arr[i], arr[i+1])
                            i = i + 2
                else:
                    i = i + 1
                
SwapPost(ARRAY1)

STRING2 = ''.join(str(x) for x in ARRAY1)

print ("AFTER IONIC CHARGE REGULATION, REVERSE SMILES NOTATION BECOME: ")
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

print("OPERATION IONIC CHARGE REPOSITIONING PERFORMED SUCCESSFULLY")



