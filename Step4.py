import os

print ("\nSTEP FOUR OF LOGICAL PROCESSOR\n")
print ("METHOD-4: OPERATION ELEMENT SYMBOL CORRECTION\n")

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

def SwapPost(arr):
    i = 0
    j = len(arr)
    while i < j-1:
        if arr[i] == 'e' and arr[i+1] == 'H':
            arr[i] = 'H'
            arr[i+1] = 'e'
            i = i + 2
        elif arr[i] == 'e' and arr[i+1] == 'N':
            arr[i] = 'N'
            arr[i+1] = 'e'
            i = i + 2
        elif arr[i] == 'r' and arr[i+1] == 'A':
            arr[i] = 'A'
            arr[i+1] = 'r'
            i = i + 2
        elif arr[i] == 'r' and arr[i+1] == 'K':
            arr[i] = 'K'
            arr[i+1] = 'r'
            i = i + 2
        elif arr[i] == 'e' and arr[i+1] == 'X':
            arr[i] = 'X'
            arr[i+1] = 'e'
            i = i + 2
        elif arr[i] == 'i' and arr[i+1] == 'L':
            arr[i] = 'L'
            arr[i+1] = 'i'
            i = i + 2
        elif arr[i] == 'a' and arr[i+1] == 'N':
            arr[i] = 'N'
            arr[i+1] = 'a'
            i = i + 2
        elif arr[i] == 'b' and arr[i+1] == 'R':
            arr[i] = 'R'
            arr[i+1] = 'b'
            i = i + 2
        elif arr[i] == 's' and arr[i+1] == 'C':
            arr[i] = 'C'
            arr[i+1] = 's'
            i = i + 2
        elif arr[i] == 'r' and arr[i+1] == 'F':
            arr[i] = 'F'
            arr[i+1] = 'r'
            i = i + 2
        elif arr[i] == 'e' and arr[i+1] == 'B':
            arr[i] = 'B'
            arr[i+1] = 'e'
            i = i + 2
        elif arr[i] == 'g' and arr[i+1] == 'M':
            arr[i] = 'M'
            arr[i+1] = 'g'
            i = i + 2
        elif arr[i] == 'a' and arr[i+1] == 'C':
            arr[i] = 'C'
            arr[i+1] = 'a'
            i = i + 2
        elif arr[i] == 'r' and arr[i+1] == 'S':
            arr[i] = 'S'
            arr[i+1] = 'r'
            i = i + 2
        elif arr[i] == 'a' and arr[i+1] == 'B':
            arr[i] = 'B'
            arr[i+1] = 'a'
            i = i + 2
        elif arr[i] == 'a' and arr[i+1] == 'R':
            arr[i] = 'R'
            arr[i+1] = 'a'
            i = i + 2
        elif arr[i] == 'c' and arr[i+1] == 'S':
            arr[i] = 'S'
            arr[i+1] = 'c'
            i = i + 2
        elif arr[i] == 'a' and arr[i+1] == 'L':
            arr[i] = 'L'
            arr[i+1] = 'a'
            i = i + 2
        elif arr[i] == 'c' and arr[i+1] == 'A':
            arr[i] = 'A'
            arr[i+1] = 'c'
            i = i + 2
        elif arr[i] == 'i' and arr[i+1] == 'T':
            arr[i] = 'T'
            arr[i+1] = 'i'
            i = i + 2
        elif arr[i] == 'r' and arr[i+1] == 'Z':
            arr[i] = 'Z'
            arr[i+1] = 'r'
            i = i + 2
        elif arr[i] == 'f' and arr[i+1] == 'H':
            arr[i] = 'H'
            arr[i+1] = 'f'
            i = i + 2
        elif arr[i] == 'f' and arr[i+1] == 'R':
            arr[i] = 'R'
            arr[i+1] = 'f'
            i = i + 2
        elif arr[i] == 'b' and arr[i+1] == 'N':
            arr[i] = 'N'
            arr[i+1] = 'b'
            i = i + 2
        elif arr[i] == 'a' and arr[i+1] == 'T':
            arr[i] = 'T'
            arr[i+1] = 'a'
            i = i + 2
        elif arr[i] == 'b' and arr[i+1] == 'D':
            arr[i] = 'D'
            arr[i+1] = 'b'
            i = i + 2
        elif arr[i] == 'r' and arr[i+1] == 'C':
            arr[i] = 'C'
            arr[i+1] = 'r'
            i = i + 2
        elif arr[i] == 'o' and arr[i+1] == 'M':
            arr[i] = 'M'
            arr[i+1] = 'o'
            i = i + 2
        elif arr[i] == 'g' and arr[i+1] == 'S':
            arr[i] = 'S'
            arr[i+1] = 'g'
            i = i + 2
        elif arr[i] == 'n' and arr[i+1] == 'M':
            arr[i] = 'M'
            arr[i+1] = 'n'
            i = i + 2
        elif arr[i] == 'c' and arr[i+1] == 'T':
            arr[i] = 'T'
            arr[i+1] = 'c'
            i = i + 2
        elif arr[i] == 'e' and arr[i+1] == 'R':
            arr[i] = 'R'
            arr[i+1] = 'e'
            i = i + 2
        elif arr[i] == 'e' and arr[i+1] == 'F':
            arr[i] = 'F'
            arr[i+1] = 'e'
            i = i + 2
        elif arr[i] == 'u' and arr[i+1] == 'R':
            arr[i] = 'R'
            arr[i+1] = 'u'
            i = i + 2
        elif arr[i] == 's' and arr[i+1] == 'O':
            arr[i] = 'O'
            arr[i+1] = 's'
            i = i + 2
        elif arr[i] == 'o' and arr[i+1] == 'C':
            arr[i] = 'C'
            arr[i+1] = 'o'
            i = i + 2
        elif arr[i] == 'h' and arr[i+1] == 'R':
            arr[i] = 'R'
            arr[i+1] = 'h'
            i = i + 2
        elif arr[i] == 'r' and arr[i+1] == 'I':
            arr[i] = 'I'
            arr[i+1] = 'r'
            i = i + 2
        elif arr[i] == 'i' and arr[i+1] == 'N':
            arr[i] = 'N'
            arr[i+1] = 'i'
            i = i + 2
        elif arr[i] == 'd' and arr[i+1] == 'P':
            arr[i] = 'P'
            arr[i+1] = 'd'
            i = i + 2
        elif arr[i] == 't' and arr[i+1] == 'P':
            arr[i] = 'P'
            arr[i+1] = 't'
            i = i + 2
        elif arr[i] == 'u' and arr[i+1] == 'C':
            arr[i] = 'C'
            arr[i+1] = 'u'
            i = i + 2
        elif arr[i] == 'g' and arr[i+1] == 'A':
            arr[i] = 'A'
            arr[i+1] = 'g'
            i = i + 2
        elif arr[i] == 'u' and arr[i+1] == 'A':
            arr[i] = 'A'
            arr[i+1] = 'u'
            i = i + 2
        elif arr[i] == 'n' and arr[i+1] == 'Z':
            arr[i] = 'Z'
            arr[i+1] = 'n'
            i = i + 2
        elif arr[i] == 'd' and arr[i+1] == 'C':
            arr[i] = 'C'
            arr[i+1] = 'd'
            i = i + 2
        elif arr[i] == 'g' and arr[i+1] == 'H':
            arr[i] = 'H'
            arr[i+1] = 'g'
            i = i + 2
        elif arr[i] == 'l' and arr[i+1] == 'A':
            arr[i] = 'A'
            arr[i+1] = 'l'
            i = i + 2
        elif arr[i] == 'a' and arr[i+1] == 'G':
            arr[i] = 'G'
            arr[i+1] = 'a'
            i = i + 2
        elif arr[i] == 'n' and arr[i+1] == 'I':
            arr[i] = 'I'
            arr[i+1] = 'n'
            i = i + 2
        elif arr[i] == 'l' and arr[i+1] == 'T':
            arr[i] = 'T'
            arr[i+1] = 'l'
            i = i + 2
        elif arr[i] == 'i' and arr[i+1] == 'S':
            arr[i] = 'S'
            arr[i+1] = 'i'
            i = i + 2
        elif arr[i] == 'e' and arr[i+1] == 'G':
            arr[i] = 'G'
            arr[i+1] = 'e'
            i = i + 2
        elif arr[i] == 'n' and arr[i+1] == 'S':
            arr[i] = 'S'
            arr[i+1] = 'n'
            i = i + 2
        elif arr[i] == 'b' and arr[i+1] == 'P':
            arr[i] = 'P'
            arr[i+1] = 'b'
            i = i + 2
        elif arr[i] == 's' and arr[i+1] == 'A':
            arr[i] = 'A'
            arr[i+1] = 's'
            i = i + 2
        elif arr[i] == 'b' and arr[i+1] == 'S':
            arr[i] = 'S'
            arr[i+1] = 'b'
            i = i + 2
        elif arr[i] == 'i' and arr[i+1] == 'B':
            arr[i] = 'B'
            arr[i+1] = 'i'
            i = i + 2
        elif arr[i] == 'e' and arr[i+1] == 'S':
            arr[i] = 'S'
            arr[i+1] = 'e'
            i = i + 2
        elif arr[i] == 'e' and arr[i+1] == 'T':
            arr[i] = 'T'
            arr[i+1] = 'e'
            i = i + 2
        elif arr[i] == 'o' and arr[i+1] == 'P':
            arr[i] = 'P'
            arr[i+1] = 'o'
            i = i + 2
        elif arr[i] == 'r' and arr[i+1] == 'B':
            arr[i] = 'B'
            arr[i+1] = 'r'
            i = i + 2
        elif arr[i] == 'l' and arr[i+1] == 'C':
            arr[i] = 'C'
            arr[i+1] = 'l'
            i = i + 2
        elif arr[i] == 't' and arr[i+1] == 'A':
            arr[i] = 'A'
            arr[i+1] = 't'
            i = i + 2
        elif arr[i] == 'e' and arr[i+1] == 'C':
            arr[i] = 'C'
            arr[i+1] = 'e'
            i = i + 2
        elif arr[i] == 'r' and arr[i+1] == 'P':
            arr[i] = 'P'
            arr[i+1] = 'r'
            i = i + 2
        elif arr[i] == 'd' and arr[i+1] == 'N':
            arr[i] = 'N'
            arr[i+1] = 'd'
            i = i + 2
        elif arr[i] == 'm' and arr[i+1] == 'P':
            arr[i] = 'P'
            arr[i+1] = 'm'
            i = i + 2
        elif arr[i] == 'm' and arr[i+1] == 'S':
            arr[i] = 'S'
            arr[i+1] = 'm'
            i = i + 2
        elif arr[i] == 'u' and arr[i+1] == 'E':
            arr[i] = 'E'
            arr[i+1] = 'u'
            i = i + 2
        elif arr[i] == 'd' and arr[i+1] == 'G':
            arr[i] = 'G'
            arr[i+1] = 'd'
            i = i + 2
        elif arr[i] == 'b' and arr[i+1] == 'T':
            arr[i] = 'T'
            arr[i+1] = 'b'
            i = i + 2
        elif arr[i] == 'y' and arr[i+1] == 'D':
            arr[i] = 'D'
            arr[i+1] = 'y'
            i = i + 2
        elif arr[i] == 'o' and arr[i+1] == 'H':
            arr[i] = 'H'
            arr[i+1] = 'o'
            i = i + 2
        elif arr[i] == 'r' and arr[i+1] == 'E':
            arr[i] = 'E'
            arr[i+1] = 'r'
            i = i + 2
        elif arr[i] == 'm' and arr[i+1] == 'T':
            arr[i] = 'T'
            arr[i+1] = 'm'
            i = i + 2
        elif arr[i] == 'b' and arr[i+1] == 'Y':
            arr[i] = 'Y'
            arr[i+1] = 'b'
            i = i + 2
        elif arr[i] == 'u' and arr[i+1] == 'L':
            arr[i] = 'L'
            arr[i+1] = 'u'
            i = i + 2
        elif arr[i] == 'h' and arr[i+1] == 'T':
            arr[i] = 'T'
            arr[i+1] = 'h'
            i = i + 2
        elif arr[i] == 'a' and arr[i+1] == 'P':
            arr[i] = 'P'
            arr[i+1] = 'a'
            i = i + 2
        elif arr[i] == 'p' and arr[i+1] == 'N':
            arr[i] = 'N'
            arr[i+1] = 'p'
            i = i + 2
        elif arr[i] == 'u' and arr[i+1] == 'P':
            arr[i] = 'P'
            arr[i+1] = 'u'
            i = i + 2
        elif arr[i] == 'm' and arr[i+1] == 'A':
            arr[i] = 'A'
            arr[i+1] = 'm'
            i = i + 2
        elif arr[i] == 'm' and arr[i+1] == 'C':
            arr[i] = 'C'
            arr[i+1] = 'm'
            i = i + 2
        elif arr[i] == 'k' and arr[i+1] == 'B':
            arr[i] = 'B'
            arr[i+1] = 'k'
            i = i + 2
        elif arr[i] == 'f' and arr[i+1] == 'C':
            arr[i] = 'C'
            arr[i+1] = 'f'
            i = i + 2
        elif arr[i] == 's' and arr[i+1] == 'E':
            arr[i] = 'E'
            arr[i+1] = 's'
            i = i + 2
        elif arr[i] == 'm' and arr[i+1] == 'F':
            arr[i] = 'F'
            arr[i+1] = 'm'
            i = i + 2
        elif arr[i] == 'd' and arr[i+1] == 'M':
            arr[i] = 'M'
            arr[i+1] = 'd'
            i = i + 2
        elif arr[i] == 'o' and arr[i+1] == 'N':
            arr[i] = 'N'
            arr[i+1] = 'o'
            i = i + 2
        elif arr[i] == 'r' and arr[i+1] == 'L':
            arr[i] = 'L'
            arr[i+1] = 'r'
            i = i + 2
        else:
            i = i + 1


SwapPost(ARRAY1)

STRING2 = ''.join(str(x) for x in ARRAY1)

print ("AFTER ELEMENT SYMBOL CORRECTION, REVERSE SMILES NOTATION BECOME: ")
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

print("STEP FOUR: OPERATION ELEMENT SYMBOL CORRECTION PERFORMED SUCCESSFULLY")



