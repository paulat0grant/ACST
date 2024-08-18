import os

print ("\nSTEP THREE OF LOGICAL PROCESSOR\n")
print ("METHOD-3: OPERATION RING DIGIT REPOSITIONING\n")

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

def swapPercentt(a, b, c):
    d = a
    a = c
    c = d
    return a, b, c

def SwapPercent(arr):
    i = 0
    j = len(arr)
    while i < j-1:
                if arr[i] == '%':
                    arr[i-2], arr[i-1], arr[i] = swapPercentt(arr[i-2], arr[i-1], arr[i])
                    i = i + 1
                else:
                    i = i + 1
                



ARRAY2 = list(STRING1)

def SwapPost(t):
    i = 0
    j = len(t)
    k = 0
    u = {}
    l = 0
    v = {}
    dd = 0
    while (i<j):
        if (t[i] == '%'):
            u[k] = t[i]
            k = k + 1
            i = i + 1
            while (t[i].isdigit()) or (t[i] == '%'):
                u[k] = t[i]
                k = k + 1
                i = i + 1
                if (i>j):
                    break
        elif t[i].isdigit():
            if t[i+1] == '-' or t[i+1] == '+':
                i=i+1
                continue
            else:
                while (t[i].isdigit()) or (t[i] == '%'):
                    u[k] = t[i]
                    k = k + 1
                    i = i + 1
                    if (i>j):
                        break
            if t[i] == '[':
                v[l] = t[i]
                while (t[i]!=']'):
                    l = l + 1
                    i = i + 1
                    v[l] = t[i]
                    if (i>j):
                        break
            elif t[i] == '(':
                v[l] = t[i]
                while (t[i]!=')'):
                    l = l + 1
                    i = i + 1
                    v[l] = t[i]
                    if (i>j):
                        break
            else:
                v[l] = t[i]
            while (dd<k):
                v[l+1] = u[dd]
                l = l + 1
                dd = dd + 1
            f = len(v)
            LL=0
            while (LL<f):
                t[i-f+1+LL]=v[LL]
                LL=LL+1
        u.clear()
        k=0
        v.clear()
        l = 0
        dd = 0
        i=i+1

SwapPost(ARRAY2)

SwapPercent(ARRAY2)

STRING3 = ''.join(str(x) for x in ARRAY2)

print ("AFTER RING DIGIT REPOSITIONING, REVERSE SMILES NOTATION BECOME: ")
print(STRING3)

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

print("STEP THREE: OPERATION RING DIGIT REPOSITIONING SUCCESSFULLY PERFORMED")

